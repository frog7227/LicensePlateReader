# main.py for the license plate reader
import cv2
import sys

# takes in the first argument as the input file name
if len(sys.argv) == 1:  # if only one argument was specified, the image file wasn't specified
    print("No image was specified")
    quit(1)  # close with error 1
img = cv2.imread(sys.argv[1])

if img is None:  # if a file name was given, but it was invalid
    print("No valid image was specified")
    quit(1)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(_, binImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
# The underscore is where the threshold goes, but we don't care about it, so trash it

cv2.imshow('Original image', img)
cv2.imshow('Binary image', binImg)
cv2.waitKey(0)  # pause so that the user can see the images
