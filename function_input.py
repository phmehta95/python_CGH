import sys
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold = sys.maxsize)
from PIL import Image
import PIL
from matplotlib import pyplot as plt
from matplotlib import image as mpimg


#Defining the function which produces a grey-level image
def function_greylevel(pathimage):
    img = Image.open(pathimage)
#    img = float(img)
    img = np.mean(img, axis = 2)
    
    #Subtract background
    img = img - img.min()
    img = img/img.max()
    #Invert greyscale
    img = 1-img
    img = img/img.sum()
    img = np.matrix.transpose(img)
    return img
#    print (type(img))
#    int8_img = img.astype(np.uint8)
#    int8_img = Image.fromarray(int8_img)
#    int8_img.save("greylevel_img.png")
#function_greylevel("Image1.jpg")
