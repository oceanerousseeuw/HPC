#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 4:
        print("usage:", sys.argv[0], "<filename> <outfile> <multi>")
        sys.exit(-1)
    FILENAME = sys.argv[1]
    OUTFILE = sys.argv[2]
    MULTI = sys.argv[3]

    # load input image
    imgIn = cv.imread(FILENAME)
    if imgIn.size == 0:
        print("failed to load", FILENAME)
        sys.exit(-1)

    # compute output image
    t0 = time.time()

    imgOut = imgIn.copy()
    #imgOut = imgOut * float(MULTI)
    imgOut = (imgOut * float(MULTI))/255
    t1 = time.time()

    # outputs
    print("time:", t1-t0, "s")
    while True:
        k = cv.waitKey() & 0xFF
        #cv.imwrite(OUTFILE, imgOut)
        cv.imshow(OUTFILE, imgOut)
        if (k == 27):
            break

