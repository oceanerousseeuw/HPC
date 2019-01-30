#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 4:
        print("usage:", sys.argv[0], "<filename> <gaussian> <sigma>")
        sys.exit(-1)
    FILENAME = sys.argv[1]
    GAUSS = int(sys.argv[2])
    SIGMA = float(sys.argv[3])

    cap = cv.VideoCapture(FILENAME)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        blur = cv.GaussianBlur(frame, (GAUSS,GAUSS), SIGMA)
        blur = cv.Canny(blur, 0, 40)

        cv.imshow('bmx', blur)
        if cv.waitKey(30) == 27:
            break


