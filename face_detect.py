import cv2 as cv

img= cv.imread("photos/lady.jpg")
cv.imshow("lady",img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + "haarcascade_frontalface_default.xml"
)  #loading the caar cascade classifier that detects the faces 

faces_rect = haar_cascade.detectMultiScale(  #searches in the image for faces at different sizes
    gray,
    scaleFactor=1.1,    #reduce the imaage scale by 10% between detection passes
    minNeighbors=3       #detemine how many neighbouts needed to be detected to accept a face , specifies the senstivety 
                        # by increasing it the model will be less senstive and more senstive i we reduce it 
)

for (x, y, w, h) in faces_rect:  #loops aver the detected faces and make a rectangle around the detected faces 
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)  #take the image,specify the coordinates of the rectangle make it green with thickness 2

cv.imshow("Face Detection", img)

print(f"Number of faces found: {len(faces_rect)}")   #specify the no of detected faces 
cv.waitKey(0)