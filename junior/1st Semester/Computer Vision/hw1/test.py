import cv2, skimage.data
import numpy as np
import matplotlib.pyplot as plt

x = skimage.data.astronaut()
my_img = cv2.imread('blue.jpeg')
img = cv2.cvtColor(my_img, cv2.COLOR_BGR2RGB)

h, w, c = x.shape


r, g, b = img[:,:,0].astype(np.float32), img[:,:,1].astype(np.float32), img[:,:,2].astype(np.float32)
print(r.dtype)

#print(np.unique(b))
numerator = 2*r - g - b
print(f"{r.shape} {g.shape} {b.shape}")

print(r[0][0])
print(g[0][0])
print(b[0][0])
print(numerator[0][0])