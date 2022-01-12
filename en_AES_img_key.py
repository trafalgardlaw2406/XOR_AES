import numpy as np
import itertools
from get_shape import get_shape
from read_txt import read_txt
from AES import en_AES
from aes_init import aes_init
from read_img import read_img
def en_AES_img_key(img,key_hex):
    l3 = []
    count = 0
    (l,m,n,z) = read_txt(img) # z is the remain 
    ciphertext_hex = l[1]
    ciphertext = np.zeros((1, len(ciphertext_hex)), dtype='int16')
    for i in range(len(ciphertext_hex)):
        ciphertext[0, i] = int(ciphertext_hex[i], 16)
    l1 = []
    [s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init(key_hex)
    for i in range(int((m*n+z)/16)):
        l1.append(en_AES(l[i],s_box, inv_s_box, w, poly_mat, inv_poly_mat).tolist())
    del l
    l3 = list(itertools.chain(*l1))
    del l1
    l4 = list(itertools.chain(*l3))
    del l3 
    if z != 0 :
        l4 = l4[:-z]
    img_txt2_cipher =  "Image_txt_cipher\\img_keycipher.txt"
    f = open(img_txt2_cipher, 'w+')
    for i in range(m*n):
        if(count == n):
            f.write("\n")
            count = 0
        x = str(l4[i])
        count = count+1
        f.write(x)
        f.write("\t")
    f.close()
    del l4
if __name__ == "__main__":
    key_hex = ['FF', '11', '12', '25', '99', 'F0', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01']
    en_AES_img_key("0003",key_hex)