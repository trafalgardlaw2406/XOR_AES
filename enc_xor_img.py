# XOR key image and the others
import pandas as pd
def xor_img(img_txt1, img_txt2):
    A = pd.read_csv(img_txt1, delimiter='\t', header = None, index_col = None)
    A = A.iloc[:,:-1]
    l1 = []
    for i in range(512):
       for j in range(512):
           l1.append(A[j][i])
    B = pd.read_csv(img_txt2, delimiter='\t', header = None, index_col = None)
    B = B.iloc[:,:-1]
    l2 = []
    for i in range(512):
       for j in range(512):
           l2.append(B[j][i])
    l3 = []
    for i in range(512*512):
        a = l1[i]^l2[i]
        l3.append(a)
    return l3

if __name__ == '__main__':
    a = "0002"
    img_txt1 = "Image_txt\\" + a + ".txt"
    b = "0012"
    img_txt2 = "Image_txt\\" + b + ".txt"
    xor_img(img_txt1,img_txt2)