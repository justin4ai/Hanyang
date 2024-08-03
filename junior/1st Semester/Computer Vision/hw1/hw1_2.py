import cv2, skimage.data
import numpy as np
import matplotlib.pyplot as plt

x = skimage.data.astronaut()
my_img = cv2.imread('alien.png')
print(my_img.dtype)
my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)
# print(f"astronaut shape : {x.shape}, my image shape : {my_img.shape}")

h, w, c = x.shape


def hw1_2(img, output_path):
    r, g, b = img[:,:,0].astype(np.float32), img[:,:,1].astype(np.float32), img[:,:,2].astype(np.float32)
    # print(f"max in r : {np.max(r)}, max in g : {np.max(g)}, max in b : {np.max(b)}")
    # print(f"min in r : {np.min(r)}, min in g : {np.min(g)}, min in b : {np.min(b)}")
    eps = 1e-15

    I = (1/3) * r + (1/3) * g + (1/3) * b


    mins = np.min(img, axis = 2)
    s = np.clip(np.where(I == 0, 0, 1 - (np.min(img, axis=2) / (I + eps))), 0, 1)


    numerator = 2*r - g - b
    denominator = 2*( ((r-g)**2 + (r-b)*(g-b))**(0.5) )   + eps
    # print(f"max in numerator : {np.max(numerator)}, min in numerator : {np.min(numerator)}")
    # print(f"max in denominator : {np.max(denominator)}, min in denominator : {np.min(denominator)}")

    v = np.clip((numerator / denominator), -1, 1)
    # print(f"v max {np.max(v)}, v min {np.min(v)}")
    h = np.arccos(v) / (2*np.pi)
    # print(f"max in h : {np.max(h)}, max in s : {np.max(s)}, max in i : {np.max(I)}")
    # print(f"min in h : {np.min(h)}, min in s : {np.min(s)}, min in i : {np.min(I)}")


    y = (77/256)*r + (150/256)*g + (29/256)*b
    cb = (-43/256)*r - (84/256)*g + (127/256)*b + 128
    cr = (127/256)*r - (106/256)*g - (21/256)*b + 128
    # print(f"max in y : {np.max(y)}, max in cb : {np.max(cb)}, max in cr : {np.max(cr)}")
    # print(f"min in y : {np.min(y)}, min in cb : {np.min(cb)}, min in cr : {np.min(cr)}")



    h = np.clip(h.copy() + 0.25, 0, 0.5)
    s = np.clip(s.copy() - 0.25, 0, 1)
    I = np.clip(I.copy() + 100, 0, 255)

    sixty = (np.pi / 3)
    h_prime = (h / sixty) * (2*np.pi) # to adjust to wikipedia
    z = 1 - abs((h_prime % 2) - 1)

    # print(f"h_prime max : {np.max(h_prime)}, min : {np.min(h_prime)}")

    i_ = I / 256

    num = (1 + z)
    c = (3*i_*s) / num
    x = c * z

    r_, g_, b_ = h_prime.copy(), h_prime.copy(), h_prime.copy()
    for i in range(len(h_prime)):
        for j in range(len(h_prime[0])):

            hp = h_prime[i][j]

            if hp == np.nan:
                r_[i][j], g_[i][j], b_[i][j] = 0, 0, 0
            elif 0 <= hp <= 1:
                r_[i][j], g_[i][j], b_[i][j] = c[i][j], x[i][j], 0
            elif 1< hp <= 2:
                r_[i][j], g_[i][j], b_[i][j] = x[i][j], c[i][j], 0            
            elif 2< hp <= 3:
                r_[i][j], g_[i][j], b_[i][j] = 0, c[i][j], x[i][j]
            elif 3< hp <= 4:
                r_[i][j], g_[i][j], b_[i][j] = 0, x[i][j], c[i][j]
            elif 4< hp <= 5:
                r_[i][j], g_[i][j], b_[i][j] = x[i][j], 0, c[i][j]
            else:
                r_[i][j], g_[i][j], b_[i][j] = c[i][j], 0, x[i][j]

    # print(f"max in r_ : {np.max(r_)}, max in g_ : {np.max(g_)}, max in b_ : {np.max(b_)}")
    # print(f"min in r_ : {np.min(r_)}, min in g_ : {np.min(g_)}, min in b_ : {np.min(b_)}")


    plt.figure(figsize=(16, 12))
    plt.subplot(431), plt.imshow(r, cmap='Reds'), plt.title('R')
    plt.subplot(432), plt.imshow(g, cmap='Greens'), plt.title('G')
    plt.subplot(433), plt.imshow(b, cmap='Blues'), plt.title('B')
    plt.subplot(434), plt.imshow(h, cmap='gray'), plt.title('H')
    plt.subplot(435), plt.imshow(s, cmap='gray'), plt.title('S')
    plt.subplot(436), plt.imshow(I, cmap='gray'), plt.title('I')
    plt.subplot(437), plt.imshow(y, cmap='gray'), plt.title('Y')
    plt.subplot(438), plt.imshow(cb, cmap='gray'), plt.title('Cb')
    plt.subplot(439), plt.imshow(cr, cmap='gray'), plt.title('Cr')
    plt.subplot(4,3,10), plt.imshow(r_, cmap='Reds'), plt.title('R\'')
    plt.subplot(4,3,11), plt.imshow(g_, cmap='Greens'), plt.title('G\'')
    plt.subplot(4,3,12), plt.imshow(b_, cmap='Blues'), plt.title('B\'')
    plt.show()
    plt.savefig(output_path)



hw1_2(x, 'x_fig_2.png')
hw1_2(my_img, 'my_fig_2.png')

