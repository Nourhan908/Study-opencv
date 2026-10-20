import cv2 as cv

img=cv.imread("photos/cats.jpg")

cv.imshow("cats",img)

#average filtering 
average_filter=cv.blur(img,(5,5))
cv.imshow("blur",average_filter)

#guassian filter
guassian=cv.GaussianBlur(img,(5,5),0)
cv.imshow("guassian",guassian)

#median
median=cv.medianBlur(img,5)
cv.imshow("median",median)

#bilaterial
bilaterail=cv.bilateralFilter(img,9,75,75)
cv.imshow("bilateral", bilaterail)
cv.waitKey(0)