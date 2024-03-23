import sys
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold = sys.maxsize)
from PIL import Image
import PIL
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import cv2

#Defining the function which produces a grey-level image
def function_greylevel(pathimage):
    img = cv2.imread(pathimage)
    
    print (img)
    img = img.astype(float)
    #img = np.mean(img, axis = 2)
    img = img/100.0
    print (img)
    #Subtract background
    img = img - img.min()
    print(img)
    img = img/img.max()
    print(img)
    #Invert greyscale
    img = 1-img
    print(img)
    img = img/img.sum()
    print(img)
    img = np.matrix.transpose(img)
    print(img)
    return img
#    print (type(img))
#    int8_img = img.astype(np.uint8)
#    int8_img = Image.fromarray(int8_img)
#    int8_img.save("greylevel_img.png")
#function_greylevel("Image1.jpg")
