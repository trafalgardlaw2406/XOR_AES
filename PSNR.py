from math import log10, sqrt
import cv2
import numpy as np
  
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  
def main():
    # compressed = cv2.imread("Image_cipher\\img__key_cipher_random.png")
    # original = cv2.imread("Image_plain\\img__key_plain_random.png", 1)
    compressed1 = cv2.imread("Image_cipher\\0003_1_cipher.png")
    original1 = cv2.imread("Image_plain\\0003_1__plain_random.png", 1)
    # value = PSNR(original, compressed)
    value1 = PSNR(original1, compressed1)
    # print(f"PSNR value is {value} dB")   
    print(f"PSNR value is {value1} dB")     
     
if __name__ == "__main__":
    main()