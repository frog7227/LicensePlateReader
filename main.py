# main.py for the license plate reader
import cv2
import sys
import numpy as np

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

# erode and dilate image to remove noise
# se = np.ones((10, 10), np.uint8)

blurred = cv2.medianBlur(binImg, 1)  # smooth out the image

#se = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
#eroded = cv2.erode(blurred, se, iterations=1)  # erode and dilate to reduce noise
#dilated = cv2.dilate(eroded, se, iterations=1)

cv2.imshow('Original image', img)
cv2.imshow('Binary image', binImg)
cv2.imshow('blurred', blurred)


cv2.waitKey(0)  # pause so that the user can see the images
