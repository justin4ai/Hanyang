import cv2, skimage.data
import numpy as np
import matplotlib.pyplot as plt

x = skimage.data.astronaut()
my_img = cv2.imread('alien.png')
my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)
print(f"astronaut shape : {x.shape}, my image shape : {my_img.shape}")

s = 1.5
t = 15
theta = np.pi/6 # 30 degrees
h, w, c = x.shape


def hw1_1(img, scaling_m, rotation_m, similarity_m, affine_m, projective_m, output_path):
    img_scaled = cv2.warpAffine(img, scaling_m, (h, w))
    img_rotated = cv2.warpAffine(img, rotation_m, (h, w))
    img_similar = cv2.warpAffine(img, similarity_m, (h, w))
    img_affine = cv2.warpAffine(img, affine_m, (h, w))
    img_projected = cv2.warpPerspective(img, projective_m, (h, w))


    plt.figure(figsize=(12, 8))
    plt.subplot(231), plt.imshow(img), plt.title('Original')
    plt.subplot(232), plt.imshow(img_scaled), plt.title('Scaling')
    plt.subplot(233), plt.imshow(img_rotated), plt.title('Rotation')
    plt.subplot(234), plt.imshow(img_similar), plt.title('Similarity')
    plt.subplot(235), plt.imshow(img_affine), plt.title('Affine')
    plt.subplot(236), plt.imshow(img_projected), plt.title('Projective')

    plt.show()
    plt.savefig(output_path)


scaling_matrix = np.array([ [s, 0, 0], [0, s, 0] ], dtype=np.float32)
rotation_matrix = np.array([ [np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0] ], dtype=np.float32)
similarity_matrix = np.array([ [s*np.cos(theta), (-s)*np.sin(theta), 0], [s*np.sin(theta), s*np.cos(theta), 0] ], dtype=np.float32)
affine_transform_matrix = np.array([ [0.5, s, t], [s, 0.5, t] ], dtype=np.float32)
projective_transform_matrix = np.array([ [1.3, 0.1, 10], [1.2, 0.9, 10], [0.001, 0.0002, 1] ], dtype=np.float32)


hw1_1(x, scaling_matrix, rotation_matrix, similarity_matrix, affine_transform_matrix, projective_transform_matrix, 'x_fig.png')
hw1_1(my_img, scaling_matrix, rotation_matrix, similarity_matrix, affine_transform_matrix, projective_transform_matrix, 'my_fig.png')


