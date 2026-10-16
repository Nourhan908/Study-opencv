import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('photos/park.jpg')
cv.imshow('Park',img)

#BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('L*a*b',lab)  # HUMAN COLOR PERCEPTION

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)  #matplotlib uses RGB color space so we need to convert the image from BGR to RGB before displaying it
plt.imshow(rgb)  #matplotlib uses RGB color space so we need to convert the image from BGR to RGB before displaying it
plt.show()  #show the image using matplotlib 

#HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

#hsv to lab
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)  #no direct to lab first convert to bgr then to lab
bgr_lab=cv.cvtColor(hsv_bgr,cv.COLOR_BGR2LAB)
cv.imshow('HSV to L*a*b',bgr_lab)



cv.waitKey(0)
