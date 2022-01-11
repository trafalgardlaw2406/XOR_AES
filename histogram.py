
import numpy as np
from matplotlib import pyplot as plt
import cv2

path = "9.png"
# path = "Image_cipher\\0003_1_cipher.png"
# path_key = "Image_cipher\\img__key_cipher.png"
# path = "Image_plain\\img__key_plain.png"
# importing required libraries of opencv
  
# reads an input image
img = cv2.imread(path,0)
  
# find frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,255])
  
# show the plotting graph of an image
plt.figure(figsize=(8,8))
plt.plot(histr)
plt.show()
plt.savefig('ddd.png')
