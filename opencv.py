
# Section 1 - Basics
# 1.Reading images and videos

import cv2 as cv

# # img = cv.imread('photos/cat.jpg')
# img = cv.imread('photos/cat_large.jpg')

# if img is None:
#     print("Image not found! Check the path.")
# else:
#     cv.imshow('Cat', img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()

# capture = cv.VideoCapture('videos/dog.mp4')    #read the video file
# while True:      #loop over the frames of the video
#     isTrue, frame = capture.read()  #read all the frames and get the frame and  if it is true and read 
#     if not isTrue:
#         break
#     cv.imshow('Video', frame)          #display the frames so they appear as a video
#     if cv.waitKey(20) & 0xFF == ord('d'):  #if the user pressed d stop playng the video
#         #wait for the user event up to 20 miliseconds and it returns a key code that represents the key pressed by the user
#         #if the user doess not press any key in 20 miliseconds it returns -1
#         #ord('d') returns the ASCII value of the character 'd' (100)
#         # 0xf is a hexadeceimal notation for 255 that is used to mask the key code to get the last 8 bits of the key code
#         #and operator is the bitwise operator that compare numbers at bit level
#         break
# capture.release()  #CLOSE THE vid reader  after the video is done playing
# cv.destroyAllWindows() #close all the windows done by opencv after the video is done playing

# #2.resizing and rescaling frames

def rescaleFrame(frame, scale=0.75):  #function that take the frame and the scale as an argument and return the resized frame
    width=int(frame.shape[1]*scale)    #widthn and height of the frame is calculated by multiplying the original width and height with the scale
    height=int(frame.shape[0]*scale)    #every image is represented as (heiht,width,channels)
    dimentions=(width,height)     #variable for the new dim to be taken in the resize function
    return cv.resize(frame,dimentions,interpolation=cv.INTER_AREA)   #retutn the resized frame using the resize function that takes the frame and the new dimentions and interpolated them by using the INTER_AREA method that is used for shrinking the image

capture = cv.VideoCapture('videos/dog.mp4')    #read the video file
while True:      #loop over the frames of the video
    isTrue, frame= capture.read()  #read all the frames and get the frame and  if it is true and read 
    if not isTrue:
        break
    resizedFrame = rescaleFrame(frame, scale=0.2) #rescale the frame
    cv.imshow('Video_rescaled', resizedFrame)          #display the frames so they appear as a video
    if cv.waitKey(20) & 0xFF == ord('d'):  #if the user pressed d stop playng the video
        #wait for the user event up to 20 miliseconds and it returns a key code that represents the key pressed by the user
        #if the user doess not press any key in 20 miliseconds it returns -1
        #ord('d') returns the ASCII value of the character 'd' (100)
        # 0xf is a hexadeceimal notation for 255 that is used to mask the key code to get the last 8 bits of the key code
        #and operator is the bitwise operator that compare numbers at bit level
        break
capture.release()  #CLOSE THE vid reader  after the video is done playing

img = cv.imread('photos/cat_large.jpg')
resized_img = rescaleFrame(img, scale=0.2) #rescale the frame
cv.imshow('Cat', resized_img)
cv.waitKey(0)
cv.destroyAllWindows() #close all the windows done by opencv after the video is done playing
# for live videos onlyyy
def changeRes(width, height):
    capture.set(3, width)  #set the width of the frame
    capture.set(4, height) #set the height of the frame  #can make many other properties of the video like brightness, contrast, etc. 
