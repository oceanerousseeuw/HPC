#!/usr/bin/env python3

import cv2 as cv
import time
import sys
import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':

    # arguments
    if len(sys.argv) != 3:
        print("usage:", sys.argv[0], "<filename> <template>")
        sys.exit(-1)
    FILENAME = sys.argv[1]
    TEMPLATE = cv.imread(sys.argv[2])


    cap = cv.VideoCapture(FILENAME)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break

        img = frame.copy()
        method = eval('cv.TM_CCOEFF_NORMED')
        res = cv.matchTemplate(frame, TEMPLATE, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        if max_val > 0.7 :
            top_left = max_loc
            bottom_right = (top_left[0] + 50, top_left[1] + 30)
            
            cv.rectangle(frame,top_left, bottom_right, 255, 2)
            plt.subplot(121),plt.imshow(res,cmap = 'gray')
            plt.subplot(122),plt.imshow(frame,cmap = 'gray')
            plt.show()

        cv.imshow('road_tracking', frame)
        if cv.waitKey(30) == 27:
            break


