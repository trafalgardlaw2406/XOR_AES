import pandas as pd
def de_xor_img(img_txt1, img_txt2):
    A = pd.read_csv(img_txt1, delimiter='\t', header = None, index_col = None)
    A = A.iloc[:,:-1]
    l1 = []
    for i in range(512):
       for j in range(512):
           l1.append(A[j][i])
    count = 0
    B = pd.read_csv(img_txt2, delimiter='\t', header = None, index_col = None)
    B = B.iloc[:,:-1]
    l2 = []
    for i in range(512):
       for j in range(512):
           l2.append(B[j][i])
    l3 = []
    for i in range(262144):
        a = l1[i]^l2[i]
        l3.append(a)
    img_txt2_cipher = "Image_txt_plant\\" + b + "_plant.txt"
    f = open(img_txt2_cipher, 'w+')
    for i in range(262144):
        if(count == 512):
            f.write("\n")
            count = 0
        a = str(l3[i])
        count = count+1
        f.write(a)
        f.write("\t")
    f.close()

if __name__ == '__main__':
    a = "0002"
    img_txt1 = "Image_txt\\" + a + ".txt"
    b = "0012"
    img_txt2 = "Image_txt_cipher\\" + b + "_cipher.txt"
    de_xor_img(img_txt1,img_txt2)