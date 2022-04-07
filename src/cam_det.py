import cv2
import image_compare as ic
from PIL import Image, ImageEnhance
import numpy as np

def from_cv_to_PIL(image):
    return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def from_PIL_to_cv(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

def cam_det(width = 64, heigh = 64, tolerance = 0):

    vid = cv2.VideoCapture(0)
    vid.set(3, width)
    vid.set(4, heigh)
    oldImg = Image.new("RGB", (width, heigh))
    oldDifferenceIndicator = 0.9
    while (True):

        ret, newFrame = vid.read()

        newImg = from_cv_to_PIL(newFrame)
        newImg = ImageEnhance.Brightness(newImg)
        newImg.enhance(1)
        newImg = newImg.image
        view = from_PIL_to_cv(newImg)
        cv2.imshow('win', view)

        newDifferenceIndicator = ic.compareImages(newImg, oldImg)
        print(abs(newDifferenceIndicator - oldDifferenceIndicator))
        if abs(newDifferenceIndicator - oldDifferenceIndicator) < tolerance:
            newImg.save("../database/brick.png", bitmap_format="png")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

cam_det()