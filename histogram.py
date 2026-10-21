import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np 

img=cv.imread("photos/cats.jpg")
cv.imshow("cats",img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

blank=np.zeros(img.shape[:2], dtype="uint8")
circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow("mask", mask)

# #hist for gray
# hist_gray=cv.calcHist([mask],[0],None,[256],[0,256]) #path the omage as it is a list , thenthe list of zero only as it is one channel , then none as no mask , then the number o bins then the range of the bins in xaxis
# plt.figure()  #make a figure 
# plt.title("histogram of gray image")
# plt.xlabel("the pixel i ntensity")   
# plt.ylabel("grequency and no of pixels with this intensity")
# plt.xlim([0,256])  #range of x axis 
# plt.plot(hist_gray)   #what to implement the visualization on  
# plt.show()  #display

#color histogram
colors = ("b", "g", "r")  #define a varaible to loop over the colors and the index

for i, color in enumerate(colors):    #loop over that variable and giev it index with i and color that is the content 
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])   #image list , loop over the indeces , apply only on the circle part 

    plt.plot(hist, color=color)   #each loop in the his plot it with the color the index is in 
    plt.xlim([0, 256])

plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.show()
cv.waitKey(0)