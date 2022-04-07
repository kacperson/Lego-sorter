from PIL import ImageChops


def compareImages(image1, image2):

    imageDifference = ImageChops.difference(image1, image2)
    pixels = list(imageDifference.getdata())
    differenceIndicator = 0
    for point in pixels:
        differenceIndicator += (point[0]+point[1]+point[2]) / 765
    differenceIndicator = differenceIndicator / len(pixels)

    return differenceIndicator
