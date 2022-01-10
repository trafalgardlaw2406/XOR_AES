# read txt file from folder Image_txt -> hex
import pandas as pd
def read_txt(img_txt):
    A = pd.read_csv(img_txt, delimiter='\t', header = None, index_col =None)
    A = A.iloc[:,:-1] # Remove final colume NaN
    l = []
    for i in range(512):
       for j in range(512):
           l.append(A[j][i])
    h = []
    for i in range(16384):
        new = []
        for j in range(16):
            new.append(hex(l[16*i+j]))   # Gather 16 values into a group
        h.append(new)
    return h
if __name__ == '__main__':
    a = "Image_txt\\0003_1.txt"
    b = read_txt(a)
    print(b)

