import cv2 as cv
img= cv.imread('photos/park.jpg')
cv.imshow('Park',img)

#converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#bluring the image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade
canny=cv.Canny(blur,125,175)  #takes the blurred imges so the edges decreases , and the two threshold values to detect the edges and they are the lower and upper threshold values for the edge detection algorithm
cv.imshow('Canny Edges',canny)

#dilating the image
dilated=cv.dilate(canny,(7,7),iterations=3)  #increases the thickness of the edges(whiteparts) by using a kernel of size 7x7 and iterating 3 times
cv.imshow('Dilated',dilated)

#eroding the image
eroded=cv.erode(dilated,(7,7),iterations=3)  #decreases the thickness of the edges(whiteparts) by using a kernel of size 7x7 and iterating 3 times
cv.imshow('Eroded',eroded)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) #take the image and resize it to 500x500 pixels using the INTER_CUBIC interpolation method that is used for enlarging the image   
cv.imshow('Resized',resized)

#cropping
cropped=img[50:200,200:400]  #take the image and crop it to the specified region of interest (ROI) by slicing the image array and taking the pixels from row 50 to 200 and column 200 to 400
cv.imshow('Cropped',cropped)

cv.waitKey(0)