from en_AES_img_key import en_AES_img_key
from enc_xor_img import xor_img
from de_AES_img_key import de_AES_img_key
import os
import time
from read_img import read_img
from gen_random import gen_random
class xor_aes:
    def __init__(self,x,key,id):
        self.key = key
        self.id = id
        self.x = x
    def encrypt(self):
        # img_key = "Image_txt\\"+ self.x + "_"+ str(self.id) + ".txt" # choose 1 frame as key img
        gen_random(512,512) # gen a random img
        img_key = "Image_txt\\random_key.txt"
        en_AES_img_key(img_key,self.key)
        files = os.listdir("Image_txt")
        l = len(files)
        # img_notkey = ["Image_txt\\"+self.x+"_"+str(i)+".txt" for i in range(1,l+1) if i != self.id] 
        img_notkey = ["Image_txt\\"+self.x+"_"+str(i)+".txt" for i in range(1,l)] 
        count = 0
        for i in range(l-1):
            xorIm = xor_img(img_key,img_notkey[i])
            img_txt2_cipher = "Image_txt_cipher\\" + self.x + "_" + str(i+1) + "_cipher.txt"
            f = open(img_txt2_cipher, 'w+')
            for i in range(512*512):
                if(count == 512):
                    f.write("\n")
                    count = 0
                a = str(xorIm[i])
                count = count+1
                f.write(a)
                f.write("\t")
            f.close()
    def decrypt(self):
        img_key = "Image_txt_cipher\\img_keycipher.txt"
        de_AES_img_key(img_key, self.key)
        imgkey_plain = "Image_txt_plain\\imgkey_plain.txt"
        l = len(os.listdir("Image_txt_cipher")) 
        imgNotkey= ["Image_txt_cipher\\"+ self.x + "_" + str(i) + "_cipher.txt" for i in range(1,l) ]
        count = 0
        for i in range(l-1):
            plainIm = xor_img(imgkey_plain,imgNotkey[i])
            img_plain_txt = "Image_txt_plain\\" + self.x + "_" + str(i+1) + "_plain.txt"
            file = open(img_plain_txt, 'w+')
            for i in range(512*512):
                if(count == 512):
                    file.write("\n")
                    count = 0
                a = str(plainIm[i])
                count = count+1
                file.write(a)
                file.write("\t")
            file.close()        
if __name__ == "__main__":
    nameFolder = "0003"
    # read_img(nameFolder)
    key = ['FF', '11', '12', '25', '99', 'F0', 'AB', '1C', '4F', '11', '14', '42', '01', '68', '97', '01']
    s = xor_aes(nameFolder, key , 1) # choose pic 1 as key
    # begin_en = time.time()
    # s.encrypt()
    # end_en = time.time()
    # print("Time to encrypt: ", end_en - begin_en)
    begin_de = time.time()
    s.decrypt()
    end_de = time.time()
    print("Time to decrypt: ", end_de - begin_de)