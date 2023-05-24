import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image a certain color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

# Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1], blank.shape[0]), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# Draw a Line
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
