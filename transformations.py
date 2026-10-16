import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('Park', img)     

#traslation
def translate (img,x,y): #function that takes the image and x for horizontal translation and y for vertical translation as arguments and return the traslated images the translated image
    transMat = np.float32([[1,0,x],[0,1,y]])  #create a transformation matrix that is used to translate the image by using the numpy float32 function that takes a 2D array as an argument and returns a 2D array of type float32
                                               # its 2d array where the first row is for the horizontal translation and the second row is for the vertical translation and the third column is for the translation values x and y
    dimensions = (img.shape[1],img.shape[0])  #specifying the dimentions of the image 
    return cv.warpAffine(img,transMat,dimensions)  #return the translated image by using the warpAffine function that takes the image, transformation matrix and dimensions as arguments
# -x to the left , x to the right , -y up , y down
rotated = translate(img,100,100)  #translate the image by 100 pixels to the right and 100 pixels down
cv.imshow('Translated',rotated)  #show the translated image

#rotation
def rotate(img,angle,rotPoint=None):  #function that takes the image and angle of rotation as arguments and return the rotated image
    (height ,width)=img.shape[:2]  #get the height and width of the image by using the shape attribute of the image and slicing it to get the first two values which are the height and width
                                    # as the shape attribute returns a tuple of three values (height, width, channels) and we only need the first two values
    if rotPoint is None:  #if the rotation point is not specified then we will use the center of the image as the rotation point
        rotPoint=(width//2,height//2)  #calculate the center of the image by using the width and height of the image and dividing them by 2
                                       #use the fllor division operator to get the integer value of the center point
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)  #create a rotation matrix that is used to rotate the image by using the getRotationMatrix2D function that takes the rotation point, angle of rotation
                                                       #the scale factor is set to 1.0 which means that the image will not be scaled and it will be rotated in its original size
    dimensions=(width,height)  #specifying the dimentions of the image
    return cv.warpAffine(img,rotMat,dimensions)  #return the rotated image by using the warpAffine function that takes the image, rotation matrix and dimensions as arguments
rotated=rotate(img,45)  #rotate the image by 45 degree
                         #+ for anticlockwise while - for clockwis
cv.imshow("rotated",rotated)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) #take the image and resize it to 500x500 pixels using the INTER_CUBIC interpolation method that is used for enlarging the image
cv.imshow("Resized",resized)

#flib
flib=cv.flip(img,0)  #0 for verticaly , 1 for horizontaly and -1 for both together 
cv.imshow("Flib",flib)

cv.waitKey(0)
