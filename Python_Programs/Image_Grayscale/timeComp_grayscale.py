import cv2 as cv
import numpy as np
import time

def format_time(seconds: float) -> str:
    if seconds >= 1:
        return f"{seconds:.3f} s"
    if seconds >= 1e-3:
        return f"{seconds*1e3:.3f} ms"
    if seconds >= 1e-6:
        return f"{seconds*1e6:.3f} µs"
    return f"{seconds*1e9:.3f} ns"

def timeit(func):
    def wrapper():
        t = time.time()
        func()
        elapsed = time.time() - t
        print(f'{func.__name__} ran in {format_time(elapsed)} seconds!')
    return wrapper



@timeit
def grayscale_cvt():
    img = cv.imread('Input\\Euro Logo.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("Output\\Euro_Logo_Gray.jpg", gray)
    # print("Auto done!")

@timeit
def grayscale_man():
    img = cv.imread('Input\\Euro Logo.jpg')
    h,w = img.shape[:2]
    gray = np.empty((h,w), dtype=np.uint8)
    for y in range(h):
        for x in range(w):
            b, g, r = img[y, x]
            val = int((0.114*b) + (0.587*g) + (0.299*r))
            gray[y, x] = np.uint8(val)
    cv.imwrite("Output\\Euro_GrayMan.jpg", gray)
    # print("manually done!") 

if __name__ == "__main__":
    grayscale_cvt()
    grayscale_man()