
# Import the modules
import cv2
from sklearn.externals import joblib
from skimage.feature import hog
import numpy as np
import shutil
import os

img = "photo.jpg"

# Load the classifier
def load():
    return joblib.load("digits_cls.pkl")

# Read the input image
def read_image():
    global img
    return cv2.imread(img)

# Convert to grayscale and apply Gaussian filtering
def pre_processing(im):
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_gray = cv2.GaussianBlur(im_gray, (5, 5), 0)
    return im_gray

# Threshold the image
def threshold(im):
    ret, im_th = cv2.threshold(im, 90, 255, cv2.THRESH_BINARY_INV)
    return im_th

# Find contours in the image
def find_contours(im):
    ret, ctrs, hier = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return ctrs

clf = load()
im = read_image()
im_gray = pre_processing(im)
im_th = threshold(im_gray)
ctrs = find_contours(im_th)

# Get rectangles contains each contour
rects = [cv2.boundingRect(ctr) for ctr in ctrs]

# For each rectangular region, calculate HOG features and predict
# the digit using Linear SVM.
def predict(clf, im, im_th, ctrs, rects):
    for rect in rects:
        # Draw the rectangles
        cv2.rectangle(im, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 3) 
        # Make the rectangular region around the digit
        leng = int(rect[3] * 1.6)
        pt1 = int(rect[1] + rect[3] // 2 - leng // 2)
        pt2 = int(rect[0] + rect[2] // 2 - leng // 2)
        roi = im_th[pt1:pt1+leng, pt2:pt2+leng]
        # Resize the image
        roi = cv2.resize(roi, (28, 28), interpolation=cv2.INTER_AREA)
        roi = cv2.dilate(roi, (3, 3))
        # Calculate the HOG features
        roi_hog_fd = hog(roi, orientations=9, pixels_per_cell=(14, 14), cells_per_block=(1, 1), visualise=False)
        nbr = clf.predict(np.array([roi_hog_fd], 'float64'))
        cv2.putText(im, str(int(nbr[0])), (rect[0], rect[1]),cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 255), 3)
    return im

#cv2.imshow("Resulting Image with Rectangular ROIs", im)
cv2.imwrite("output.jpg", predict(clf, im, im_th, ctrs, rects))
#cv2.waitKey()
