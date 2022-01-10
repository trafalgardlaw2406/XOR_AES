import numpy as np
import itertools
from read_txt import read_txt
from AES import de_AES
from aes_init import aes_init

def de_AES_img_key(img, key_hex):
    l3 = []
    l = read_txt(img)  
    ciphertext_hex = l[1]
    ciphertext = np.zeros((1, len(ciphertext_hex)), dtype='int16')
    for i in range(len(ciphertext_hex)):
        ciphertext[0, i] = int(ciphertext_hex[i], 16)
    l1 = []
    [s_box, inv_s_box, w, poly_mat, inv_poly_mat] = aes_init(key_hex)
    for i in range(16384):
        l1.append(de_AES(l[i],s_box, inv_s_box, w, poly_mat, inv_poly_mat).tolist())
    del l
    l3 = list(itertools.chain(*l1))
    del l1
    l4 = list(itertools.chain(*l3))
    del l3
    print(l4)
    img_plain_txt = "Image_txt_plain\\imgkey_plain.txt"
    f = open(img_plain_txt, 'w+')
    count = 0
    for i in range(512*512):
        if(count == 512):
            f.write("\n")
            count = 0
        x = str(l4[i],encoding='utf-8')
        count = count+1
        f.write(x)
        f.write("\t")
    f.close()
    del l4
if __name__ == "__main__":
    x = "Image_txt_cipher\\img_keycipher.txt"
    key = ['FF', '11', '12', '25', '99', 'F0', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01']
    de_AES_img_key(x,key)