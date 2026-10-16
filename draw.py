import cv2 as cv
import numpy as np

# img = cv.imread('photos/cat.jpg')
# cv.imshow('Cat', img)      #can draw on it but we want blank 
# cv.waitKey(0) 
blank=np.zeros((500,500,3),dtype='uint8')  #create a blank image of 500x500 pixels with 3 channels (RGB) and data type uint8 that refers to image 
cv.imshow('Blank',blank)  #show the blank image

blank[:]=0,255,0  #change the color of the blank image by assigning the color values to the entire image.
cv.imshow('Green',blank)  #show the green blank image
blank[0:250,0:250]=0,0,255  #change the color of the blank image by assigning the color values to a specific region of the image.
cv.imshow('Red',blank)  #show the red blank image

cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)  #draw a rectangle on the blank image with the specified coordinates, color and thickness
cv.imshow('Rectangle',blank)  #show the rectangle on the blank image

cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=3)  #draw a rectangle on the blank image with the specified coordinates, color and thickness
cv.imshow('Rectangle',blank)  #show the rectangle on the blank image

cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(255,0,0),thickness=-1)  #draw a circle on the blank image with the specified center, radius, color and thickness
cv.imshow('Circle',blank)  #show the circle on the blank image

cv.line(blank,(50,50),(130,130),(255,255,255),thickness=4)  #draw a line on the blank image with the specified start and end points, color and thickness
cv.imshow('Line',blank)  #show the line on the blank image

cv.putText(blank,'Hello World, i am nourhan khaled',(20,20),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)  #draw text on the blank image with the specified text, position, font, scale, color and thickness
cv.imshow('Text',blank)  #show the text on the blank image
cv.waitKey(0)
cv.destroyAllWindows()  #close all the windows done by opencv after the video is done playing