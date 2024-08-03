import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
from PIL import Image

def psnr(img1, img2):
    h, w = img2.shape
    mse = np.mean((img1[:h, :w] - img2)**2)

    return 10*math.log10( (255 - 0)**2 / mse )

def filtering(image, kernel):
    m, n = kernel.shape
    y, x = image.shape
    y = y - m + 1
    x = x - m + 1
    new_image = np.zeros((y, x))
    for i in range(y):
        for j in range(x):
            new_image[i][j] = np.sum(image[i:i+m, j:j+m] * kernel)

    return new_image

def hw2_1(img):

    def mean_filter(k):
        return (1 / (k)**2 ) * np.ones((k, k))


    mu, sigma = 0, 50
    noise = np.random.normal(mu, sigma, img.shape)
    img_noise = img.copy() + noise
    img_noise = np.clip(img_noise, 0, 255).astype(np.uint8)
    cv2.imwrite('justin_noise.jpeg', img_noise)

    mean_3 = filtering(img_noise, mean_filter(3))
    mean_5 = filtering(img_noise, mean_filter(5))
    mean_7 = filtering(img_noise, mean_filter(7))

    plt.figure(figsize=(6, 12))
    plt.subplot(131), plt.imshow(mean_3, cmap='gray'), plt.title('3x3 mean')
    plt.subplot(132), plt.imshow(mean_5, cmap='gray'), plt.title('5x5 mean')
    plt.subplot(133), plt.imshow(mean_7, cmap='gray'), plt.title('7x7 mean')
    plt.show()
    plt.savefig('justin_mean_filters.jpeg',  dpi=200)
    
    psnr_3 = psnr(img_noise, mean_3) 
    psnr_5 = psnr(img_noise, mean_5)
    psnr_7 = psnr(img_noise, mean_7)

    print(f"PSNR for 3x3 mean filtered noisy image : {psnr_3}\nPSNR for 5x5 mean filtered noisy image : {psnr_5}\nPSNR for 7x7 mean filtered noisy image : {psnr_7}")

def hw2_2(img):
    def sharp_filter(k):
        e = np.zeros((k, k))
        e[k//2, k//2] = 2

        return e - (1/(k**2)) * (np.ones((k, k)))
    
    sharp_3 = filtering(img, sharp_filter(3))
    sharp_5 = filtering(img, sharp_filter(5))
    sharp_7 = filtering(img, sharp_filter(7))

    plt.figure(figsize=(6, 12))
    plt.subplot(131), plt.imshow(sharp_3, cmap='gray'), plt.title('3x3 unsharp')
    plt.subplot(132), plt.imshow(sharp_5, cmap='gray'), plt.title('5x5 unsharp')
    plt.subplot(133), plt.imshow(sharp_7, cmap='gray'), plt.title('7x7 unsharp')
    plt.show()
    plt.savefig('justin_unsharp_filters.jpeg',  dpi=200)


def hw2_3(img):

    def stretch_func(u):
        if u < 100:
            return (0.8) * u

        elif 100 <= u < 200:
            return 1.5*(u-100) + 80

        else:
            return (25/55) * (u-200) + 230

    def contrast_stretch(img):

        vec_func = np.vectorize(stretch_func)
        return vec_func(img.copy())

    def gamma_correction(img):
        gamma = 2.20
        new_img = (img.copy()).astype(np.float32)
        new_img = (((new_img / 255)) ** (2.20)) * 255
        return new_img.astype(np.uint8)

    stretched_img = contrast_stretch(img)
    gamma_corrected_img = gamma_correction(img)

    plt.figure(figsize=(6, 12))
    plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('orig')
    plt.subplot(132), plt.imshow(stretched_img, cmap='gray'), plt.title('contrasting stretching')
    plt.subplot(133), plt.imshow(gamma_corrected_img, cmap='gray'), plt.title('gamma correction')
    plt.show()
    plt.savefig('justin_contrast_stretched.jpeg',  dpi=200)
    

def hw2_4(img):
    def histogram_equalization(img):

        histo, bins = np.histogram(img.flatten(), 256, [0, 256])
        cdf = histo.cumsum()

        func = (255 * (cdf / cdf[-1])).astype(np.uint8)
        img_equalized = img.copy()
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img_equalized[i, j] = func[int(img[i, j])]

    
        cv2.imwrite('justin_equalized.jpeg', img_equalized)
        histo_after = np.histogram(img_equalized.flatten(), 256, [0, 256])

        bin_centers = 0.5 * (bins[:-1] + bins[1:])

        plt.figure(figsize=(10, 6))
        plt.subplot(131)
        plt.imshow(img_equalized, cmap='gray')
        plt.title('Equalized Image')
        plt.axis('off') 

        plt.subplot(132)
        plt.bar(bin_centers, histo, width=1.0, color='b', label='Hist of Original Img')
        plt.plot(histo.cumsum(), color='orange', label='CDF of Original Img')
        plt.legend(loc='upper right')
        plt.title('Original Histogram')

        plt.subplot(133)
        plt.bar(bin_centers, histo_after[0], width=1.0, color='b', label='Hist of Equalized Img')
        plt.plot(histo_after[0].cumsum(), color='orange', label='CDF of Equalized Img')
        plt.legend(loc='upper right')
        plt.title('Equalized Histogram')

        plt.tight_layout() 
        plt.show()
        plt.savefig('justin_histo_equalization.jpeg', dpi=200)


    histogram_equalization(img)

def hw2_5(img):
    
    print(img.shape)
    image_downsampled = Image.fromarray(img).resize((img.shape[1]//4, img.shape[0]//4), Image.NEAREST)
    print(np.array(image_downsampled).shape)
    img_nearest = image_downsampled.resize((img.shape[1], img.shape[0]), Image.NEAREST)
    print(np.array(img_nearest).shape)
    img_bilinear = image_downsampled.resize((img.shape[1], img.shape[0]), Image.BILINEAR)
    img_bicubic = image_downsampled.resize((img.shape[1], img.shape[0]), Image.BICUBIC)

    plt.figure(figsize=(6, 12))
    plt.subplot(141), plt.imshow(img, cmap='gray'), plt.title('Original image')
    plt.subplot(142), plt.imshow(img_nearest, cmap='gray'), plt.title('Nearest')
    plt.subplot(143), plt.imshow(img_bilinear, cmap='gray'), plt.title('Bilinear')
    plt.subplot(144), plt.imshow(img_bicubic, cmap='gray'), plt.title('Bicubic')
    plt.show()
    plt.savefig('justin_reconstructed.jpeg',  dpi=200)


    psnr_nearest = psnr(img, np.array(img_nearest).astype(np.float64))
    psnr_bilinear = psnr(img, np.array(img_bilinear).astype(np.float64)) 
    psnr_bicubic = psnr(img, np.array(img_bicubic).astype(np.float64))
    print(f"PSNR for upsampled image by nearest : {psnr_nearest}\nPSNR for upsampled image by bilinear : {psnr_bilinear}\nPSNR for upsampled image by bicubic : {psnr_bicubic}")

if __name__ == '__main__':
    img = cv2.imread('justin.jpeg', cv2.IMREAD_GRAYSCALE).astype(np.float64)
    np.random.seed(7)

    hw2_1(img)
    hw2_2(img)
    hw2_3(img)
    hw2_4(img)
    hw2_5(img)






    












