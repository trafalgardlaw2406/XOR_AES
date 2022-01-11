import random
random.seed(1)

def gen_random(x,y):
    a = []
    for i in range(x*y):
        a.append(random.randrange(0,255))
    count = 0
    img_random_cipher = "Image_txt\\random_key.txt"
    f = open(img_random_cipher,'w+')
    for i in range(x*y):
        if(count == y):
            f.write("\n")
            count = 0
        count = count +1
        f.write(str(a[i]))
        f.write("\t")
    f.close()

gen_random(512,512)

