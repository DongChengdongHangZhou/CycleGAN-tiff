import cv2
import os
import torch
import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt

img = tiff.imread('0_B_fake_B.tiff')
img = (0.5*img+0.5)*255
plt.subplot(111),plt.imshow(img,cmap='gray'),plt.title('magnitude')
plt.savefig('save.jpg')
plt.show()


