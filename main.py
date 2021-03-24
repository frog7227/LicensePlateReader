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

# cv2.imshow('image', img)
# cv2.waitKey(0)
