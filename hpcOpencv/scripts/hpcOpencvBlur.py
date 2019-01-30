#!/usr/bin/env python3

import cv2 as cv
import time
import sys

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 5:
        print("usage:", sys.argv[0], "<filename> <outfile> <time> <filterLevel>")
        sys.exit(-1)
    FILENAME = sys.argv[1]
    OUTFILE = sys.argv[2]
    TIME = sys.argv[3]
    FILTER = sys.argv[4]

    # load input image
    imgIn = cv.imread(FILENAME)
    if imgIn.size == 0:
        print("failed to load", FILENAME)
        sys.exit(-1)

    # compute output image
    t0 = time.time()

    #imgOut = imgIn / 2
    imgOut = imgIn.copy()
    for i in range(0, int(TIME)) :
        imgOut= cv.blur(imgIn,(int(FILTER), int(FILTER)))
    
    t1 = time.time()

    # outputs
    print("time:", t1-t0, "s")
    cv.imwrite(OUTFILE, imgOut)

