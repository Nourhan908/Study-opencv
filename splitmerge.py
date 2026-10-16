import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Park', img)

blank=np.zeros(img.shape[:2],dtype="uint-8")
cv.imshow("blank",blank)

#splitting the image into its color channels
b,g,r=cv.split(img)  #split the image into its color channels by using the split function that takes the image as an argument and returns the blue, green and red channels of the image
cv.imshow('Blue',b)  #show the blue channel of the image
                     #the brighter parts indicated concentration of blue 
cv.imshow('Green',g)  #show the green channel of the image
cv.imshow('Red',r)  #show the red channel of the image

#merging the color channels back into a single image
merged=cv.merge([b,g,r])  #merge the color channels back into a single image by using the merge function that takes a list of the color channels as an argument and returns the merged image
cv.imshow('Merged',merged)  #show the merged image



cv.waitKey(0)