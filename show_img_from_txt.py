import pandas as pd
import numpy as np
import cv2

def show_img(x):
    A = pd.read_csv(x, delimiter='\t', header = None, index_col =None)
    A = A.iloc[:,:-1]
    l = []
    for i in range(512):
       for j in range(512):
           l.append(A[j][i])
    img_cipher = cv2.imread("Image\\0002.png")
    for i in range(512):
       for j in range(512):
        c = l[i*512+j]
        b = (c,c,c)
        img_cipher[i][j] = b
    # sv2.imwrite()
    cv2.imshow('Display Image', img_cipher)
    cv2.waitKey(0)
if __name__ == '__main__':
    x = "Image_txt_cipher\\imgkey_plain.txt"
    show_img(x)