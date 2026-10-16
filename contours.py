import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# #bluring the image
# blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

#canny
canny=cv.Canny(img,125,255)
cv.imshow('Canny',canny)

# #thresholding
# _, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)

#finding contours
contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
                               #takes the canny image and finds the contours of the objects in the image by using the findContours function that takes the canny image, contour retrieval mode and contour approximation method as arguments
                               #the conytours aproximate method is used to compress the contours by removing the redundant points and keeping only the essential points that define the shape of the object
                               #hierarchies is a list of the contours and their corresponding hierarchy information that is used to determine the relationship between the contours and their parent-child relationship
print(f'{len(contours)} contours found!')  #print the number of contours found in the image

#DRAWING CONTOURS
blank = np.zeros(img.shape, dtype='uint8')  #create a blank image of the same size as the original image with 3 channels (RGB) and data type uint8 that refers to image
cv.imshow('Blank', blank)  #show the blank image
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)  #draw the contours on the blank image with the specified color and thickness
cv.imshow('Contours Drawn', blank)  #show the contours drawn on the blank image
cv.waitKey(0)