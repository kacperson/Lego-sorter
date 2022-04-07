import cv2
import image_compare as ic
from PIL import Image
import numpy as np
w, h = 64, 64

vid = cv2.VideoCapture(0)
vid.set(3, w)
vid.set(4, h)
oldImg = Image.new("RGB", (w, h))

while (True):

    ret, newFrame = vid.read()
    cv2.imshow('frame', newFrame)
    newImg = Image.fromarray(cv2.cvtColor(newFrame, cv2.COLOR_BGR2RGB))

    differenceIndicator = ic.compareImages(newImg, oldImg)
    print(differenceIndicator)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()