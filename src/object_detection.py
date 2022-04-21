import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np


def crop_image(image="../database/brick.png"):
    image = cv2.imread(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    binary = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)[1]
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #contours = imutils.grab_contours(contours)
    c = max(contours, key=cv2.contourArea)


    #cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
    (x, y, w, h) = cv2.boundingRect(c)
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    #approximation to rectangle
    plt.imshow(image)
    plt.show()

crop_image()