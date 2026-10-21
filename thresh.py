import cv2 as cv 

img=cv.imread("photos/cats.jpg")
cv.imshow("cats", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#simple thresholding
threshold, thresh = cv.threshold(       #THRESHOLD returns the same value while thresh returns after threshilding , path the image , the threshold value , the max value,apply binarybthreshold 
    gray, 150, 255, cv.THRESH_BINARY
)

threshold, thresh_inv = cv.threshold(   #applying inverse binary threshold , where the imges coloris in verted where the above is now blacke and te below is white 
    gray, 150, 255, cv.THRESH_BINARY_INV
)

cv.imshow("Gray", gray)
cv.imshow("Simple Threshold", thresh)
cv.imshow("Simple Threshold inverse ", thresh_inv)

#adaptive thresholding   #the co,puter calculates an optimum threshold value 
thresha = cv.adaptiveThreshold(
    gray, 255,
    cv.ADAPTIVE_THRESH_GAUSSIAN_C,   #apply on gray image , the max value , apply guassian thresholding , the thresholding is binary type , the size of the kernel is 11 and subract 3 from each local threshold 
    cv.THRESH_BINARY,
    11, 3
)
cv.imshow("Adaptive Threshold", thresha)

threshi = cv.adaptiveThreshold(
    gray, 255,
    cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv.THRESH_BINARY_INV,
    11, 3
)


cv.imshow("Adaptive Inverse Threshold", threshi)



cv.imshow("Adaptive Threshold", thresh)



cv.waitKey(0)