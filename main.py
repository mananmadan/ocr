import cv2
import numpy as np
import matplotlib.pyplot as plt

from predict import final_predict
from align import alignImages

def plot(img):
    plt.imshow(img)
    plt.show()

img = cv2.imread("image.jpeg")
template = cv2.imread("template.jpeg")
#plot(template)
aligned = alignImages(img,template)

## define roi on the basis of template images
roi_name = ["email","first name","contact number"]
roi_x = [(100,300),(209,415),(580,742)]
roi_y = [(350,375),(316,340),(338,359)]

## loop over roi and get the final images
for i in range(0,len(roi_x)):
    print(roi_name[i]+":") 
    image = aligned[roi_y[i][0]:roi_y[i][1],roi_x[i][0]:roi_x[i][1],:]
    cv2.imwrite(roi_name[i]+'.jpeg',image)
    final_predict(aligned[roi_y[i][0]:roi_y[i][1],roi_x[i][0]:roi_x[i][1],:])