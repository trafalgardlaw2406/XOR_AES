# read txt file from folder Image_txt -> hex
import pandas as pd
def read_txt(img_txt):
    A = pd.read_csv(img_txt, delimiter='\t', header = None, index_col =None)
    A = A.iloc[:,:-1] # Remove final colume NaN
    l = []
    (a,b) = A.shape
    # print(A[b][a])
    for i in range(b):
       for j in range(a):
           l.append(A[j][i])
    h = []
    z= 0 
    if ((a*b)%16 != 0) :
        z = 16-(a*b)%16
        for j in range(16-(a*b)%16):
            l.append(0)
    for i in range(int(a*b/16)):
        new = []
        for j in range(16):
            new.append(hex(l[16*i+j]))   # Gather 16 values into a group
        h.append(new)
    
    return (h,a,b,z) # pixel value, shape (a,b) , remain z
if __name__ == '__main__':
    a = "Image_txt\\0003_5.txt"
    (h,m,n,z) = read_txt(a)
    print(m,n,z)

  

