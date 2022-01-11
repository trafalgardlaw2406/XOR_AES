import pandas as pd
import numpy as np
import cv2
import os 
def show_img(x):
    A = pd.read_csv(x, delimiter='\t', header = None, index_col =None)
    A = A.iloc[:,:-1]
    l = []
    for i in range(512):
       for j in range(512):
           l.append(A[j][i])
    img_cipher = cv2.imread("Image\\0002.png") # picture with shape (512,512,3)
    for i in range(512):
       for j in range(512):
        c = l[i*512+j]
        b = (c,c,c)
        img_cipher[i][j] = b
    # imgName = "Image_cipher\\" + x[17:24] + "_cipher.png"
    imgName = "Image_plain\\" + x[16:23] + "_plain_random.png"
    cv2.imwrite(imgName, img_cipher)
    # cv2.imshow('Display Image', img_cipher)
    # cv2.waitKey(0)
if __name__ == '__main__':
    x = "0003"
    l = len(os.listdir("Image_txt_cipher")) 
    # imgName = ["Image_txt_cipher\\"+ x + "_" + str(i) + "_cipher.txt" for i in range(1,l) ]
    imgName = ["Image_txt_plain\\"+ x + "_" + str(i) + "_plain.txt" for i in range(1,l) ]
    for i in range(l-1):
        show_img(imgName[i])
    img_key =  "Image_txt_cipher\\img_keycipher.txt"
    show_img(img_key)


    