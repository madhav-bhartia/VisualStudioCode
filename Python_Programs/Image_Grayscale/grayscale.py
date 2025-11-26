import cv2 as cv
import numpy as np

def grayscale_cvt():
    img = cv.imread('Input\\BMU_Logo.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("Output\\BMU_Logo_Gray.jpg", gray)

if __name__ == "__main__":
    grayscale_cvt()