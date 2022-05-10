import cv2
import image_compare as ic
from PIL import Image
import numpy as np
import time
import object_detection as od


def from_cv_to_PIL(image):
    return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def from_PIL_to_cv(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def image_sharpening(image):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-3, kernel=kernel)
    return image_sharp

def image_contrasting(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    cv2.imshow("lab", lab)

    # -----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)

    # -----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)


    # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl, a, b))


    # -----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    return final

def increase_brightness(image, val):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    lim = 255 - val
    v[v > lim] = 255
    v[v <= lim] += val
    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image


def cam_det(vid=cv2.VideoCapture(0), width=256, height=256, tolerance=0.005, oldDifferenceIndicator=0):

    vid.set(3, width)
    vid.set(4, height)
    oldImg = Image.new("RGB", (width, height))
    brick = -1

    ret, newFrame = vid.read()
    newFrame = increase_brightness(newFrame, 10)
    newFrame = image_sharpening(newFrame)
    newFrame = image_contrasting(newFrame)
    newImg = from_cv_to_PIL(newFrame)
    #cv2.imshow('win', newFrame)

    newDifferenceIndicator = ic.compare_images(newImg, oldImg)

    #if the difference is greater than some  tolerance take a screenshot
    if abs(newDifferenceIndicator - oldDifferenceIndicator) > tolerance or oldDifferenceIndicator == 0:
        print(abs(newDifferenceIndicator - oldDifferenceIndicator))
        oldDifferenceIndicator = newDifferenceIndicator
        time.sleep(0.3)
        #save picture
        ret, newFrame = vid.read()
        brick = od.object_det(newFrame)



    return oldDifferenceIndicator, brick

