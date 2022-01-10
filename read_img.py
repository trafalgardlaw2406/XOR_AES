# Read DiCOM image from folder 
def read_img(nameFolder):
	import cv2
	import os
	path = "Image\\"+nameFolder
	listIm = os.listdir(path)
	temp = 1
	for i in listIm:
		img_png = str()
		img_png = path+"\\"+i
		img_txt = "Image_txt\\"+ nameFolder +"_"+str(temp)+".txt"
		img = cv2.imread(img_png)
		(h, w, d) = img.shape
		# print("width={}, height={}, depth={}".format(w, h, d))
		temp += 1
		f = open(img_txt, 'w+')
		for i in range(h):
			for j in range(w):
				(a,b,c) = img[i, j] # get value of one channel
				a = str(a) 
				f.write(a)
				f.write("\t")
			f.write("\n")
		f.close()
if __name__ == '__main__':
	read_img("0003")
