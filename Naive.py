from en_AES_img_key import en_AES_img_key
from de_AES_img_key import de_AES_img_key
import os
import time
from read_img import read_img

class aes_naive:
    def __init__(self,x,key):
        self.key = key
        self.x = x
    def encrypt(self):
        files = os.listdir("Image_txt")
        l = len(files)
        for i in range(l):
            img_key = "Image_txt\\"+ self.x + "_"+ str(i+1) + ".txt"
            en_AES_img_key(img_key,self.key)
        
    def decrypt(self):
        img_key = "Image_txt_cipher\\img_keycipher.txt"
        files = os.listdir("Image_txt")
        l = len(files)
        for i in range(l):
            img_key = "Image_txt\\"+ self.x + "_"+ str(i+1) + ".txt"
            de_AES_img_key(img_key,self.key)        
if __name__ == "__main__":
    nameFolder = "0003"
    # read_img(nameFolder)
    key = ['FF', '11', '12', '25', '99', 'F0', 'AB', '1C', '4F', '11', '14', '42', '01', '68', '97', '01']
    s = aes_naive(nameFolder, key) 
    begin_en = time.time()
    s.encrypt()
    end_en = time.time()
    print("Time to encrypt in naive algorithm: ", end_en - begin_en)
    begin_de = time.time()
    s.decrypt()
    end_de = time.time()
    print("Time to decrypt in naive algorithm: ", end_de - begin_de)