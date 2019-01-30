#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], "<filename>")
        sys.exit(-1)
    FILENAME = sys.argv[1]

    # load input image
    imgIn = cv.imread(FILENAME)
    imgIn = imgIn / 255
    if imgIn.size == 0:
        print("failed to load", FILENAME)
        sys.exit(-1)

    # compute output image
    t0 = time.time()

    # fonction de rappel pour le trackbar (capture imgInput)
    def update_win(x):
        img = imgIn * x /100
        cv.imshow('image', img)

    # affiche l'image + trackbar
    cv.namedWindow('image')
    cv.createTrackbar('seuil', 'image', 0, 100, update_win)
    cv.setTrackbarPos('seuil', 'image', 50)


    t1 = time.time()
    # outputs
    print("time:", t1-t0, "s")
    while True:
        k = cv.waitKey() & 0xFF
        #cv.imwrite(OUTFILE, imgOut)
        cv.imshow(OUTFILE, imgOut)
        if (k == 27):
            break

