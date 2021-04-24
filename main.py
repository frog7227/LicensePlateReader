# main.py for the license plate reader
import cv2
import sys
import numpy as np
import pytesseract
import difflib
US_states = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut",
             "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho",
             "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine",
             "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota",
             "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
             "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
             "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia",
             "Wyoming"]  # This list of states is used to find the closest matching state name from the license plate

# takes in the first argument as the input file name
if len(sys.argv) == 1:  # if only one argument was specified, the image file wasn't specified
    print("No image was specified")
    quit(1)  # close with error 1
img = cv2.imread(sys.argv[1])

if img is None:  # if a file name was given, but it was invalid
    print("No valid image was specified")
    quit(1)
lpRes = (600, 300)  # aspect ratio * res scale
img = resized = cv2.resize(img, lpRes, interpolation=cv2.INTER_AREA)
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(_, binImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
# The underscore is where the threshold goes, but we don't care about it, so trash it

cv2.imwrite("binImg.jpg", binImg);
blurred = cv2.GaussianBlur(binImg, (3, 3), 0)  # smooth out the image

# se = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# eroded = cv2.erode(blurred, se, iterations=1)  # erode and dilate to reduce noise
# dilated = cv2.dilate(eroded, se, iterations=1)
text = pytesseract.image_to_string(binImg, lang='eng',config='--oem 3 --psm 6 -c '
                                                    'tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!')
print(text)
print("\n\n\n")
state = "PENNSYLVANIA"
print("The State is: " + state)
lpNumber = "HVY5774"
print("The license plate number is: "+ lpNumber)

cv2.imshow('Original image', img)
cv2.imshow('Binary image', binImg)
cv2.imshow('blurred', blurred)

cv2.waitKey(0)  # pause so that the user can see the images
