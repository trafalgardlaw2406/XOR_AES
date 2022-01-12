import cv2
import os
def get_shape(folderName):
   
    img_path = "Image\\" + folderName
    list_im = os.listdir(img_path)
    img_path = img_path +"\\" + list_im[0]
    # print(img_path)
    im = cv2.imread(img_path)
    a,b,c = im.shape
    return (a,b)

print(get_shape("0003"))