import os, os.path
import cv2
import pandas as pd
import itertools
from AES import en_AES
from aes_init import aes_init
# path = "Image\\0003"
# listim = os.listdir(path)
# print(listim)
# im = cv2.imread(path + "\\"+ listim[1])
# print(im.shape)
# for i in listim:
#     im = cv2.imread(i)
# img_txt = "Image_txt\\0003_1.txt"
# A = pd.read_csv(img_txt, delimiter='\t', header = None, index_col =None)
# A = A.iloc[:,:-1]
# print(A.shape)
# print(A)
# def read_txt(img_txt):
#     A = pd.read_csv(img_txt, delimiter='\t', header = None, index_col =None)
#     # A = A.iloc[:,:-1] # Remove final colume NaN
#     l = []
#     (h,w) = A.shape
#     for i in range(h):
#        for j in range(w):
#            l.append(A[j][i])
#     h = []
#     for i in range(2):
#         new = []
#         for j in range(11):
#             new.append(hex(l[11*i+j]))
#         h.append(new)
#     return h

# a = "Image_txt\\a.txt"
# b = read_txt(a)
# print(b)

# l1 = [[1,2,3],[4,5,6]]
# l2 = [7,8,9,10]
# l3 = list(itertools.chain(*l1))
# print(l3[2:])

# x = [i for i in range(9) if i!= 3]
# print(x)

# y = "avdsfsdf.txt"
# print(y[2:-4])
key = ['FF', '11', '12', '25', '99', 'F0', 'AB', '1C', '4F', '11', '14', '42', '01', '68', '97', '01']
[s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init(key)
l = "FF123"
a = en_AES(l,s_box, inv_s_box, w, poly_mat, inv_poly_mat)
print(a)
