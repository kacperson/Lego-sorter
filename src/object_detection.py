import cv2
from CNN import prediction

#acceptable opencv format
def object_det(image):

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    binary = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)[1]
    brick = -1
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    try:
        c = max(contours, key=cv2.contourArea)
        (x, y, w, h) = cv2.boundingRect(c)
        margin = 0
        if y > 10 and x > 10:
            margin = 10
        image = image[y - margin:y + h + margin, x - margin:x + w + margin]
        image = cv2.resize(image, (64, 64))
        cv2.imwrite("../CNN/brick.png", image)
        brick = prediction.make_pred("D:/Lego-sorter/CNN/brick.png")
    except ValueError:
        print("Object not detected")

    return brick


