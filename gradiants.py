import cv2 as cv

img = cv.imread("photos/cats.jpg")

cv.imshow("Original", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#laplacian     it sees the sudden change i=o pixels and make it an edge
lap = cv.Laplacian(gray, cv.CV_64F)    #take the grey image then takes the sudden change of pixels intensity as 64 bit floating poits including positive and negative 
lap = cv.convertScaleAbs(lap)   #take the absolute of the values and convert it to 8 bit image where it ranges from 0 to 255


cv.imshow("Laplacian", lap)

#sobel  measure the change by using the derivative and path kernels through image 

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=3)  #take the gray image , use floating point output , speciy the x axis the horizontal changes , kernel size 3
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=3)  #take the gray image , use floating point output , speciy the y axisv the vertical change , kernel size 3

sobelx = cv.convertScaleAbs(sobelx)      #conver the floating point output to range from 0 to 255
sobely = cv.convertScaleAbs(sobely)

combined = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  #combine the xsible and give it weight 0.5 with the ysoble with weight 0.5 and 0 is an extra brightness offset


cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)
cv.imshow("Combined Sobel", combined)

#canny    produce clean, thin edges. It combines multiple processing steps rather than simply calculating one derivative.
blur = cv.GaussianBlur(gray, (5, 5), 0)  #reduce noise 

canny = cv.Canny(blur, 100, 200)   #lower threshold , upper threshold

cv.imshow("Canny Edges", canny)

cv.waitKey(0)