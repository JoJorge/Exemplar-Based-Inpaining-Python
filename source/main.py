#!/usr/bin/python
# python 2.7 with opencv 3.4.0

import sys, os
import cv2
import numpy as np
from Inpainter import Inpainter

if __name__ == "__main__":
    """
    Usage: python main.py pathOfInputImage pathOfMaskImage [,halfPatchWidth=4].
    """
    if not len(sys.argv) == 4 and not len(sys.argv) == 5:
        print 'Usage: python main.py pathOfInputImage pathOfMaskImage [,halfPatchWidth].'
        exit(-1)
    
    if len(sys.argv) == 4:
        halfPatchWidth = 4
    elif len(sys.argv) == 5:
        try:
            halfPatchWidth = int(sys.argv[4])
        except ValueError:
            print 'Unexpected error:', sys.exc_info()[0]
            exit(-1)
    
    # image File Name
    imageName = sys.argv[1]
    # CV_LOAD_IMAGE_COLOR: loads the image in the RGB format TODO: check RGB sequence
    originalImage = cv2.imread(imageName, cv2.IMREAD_COLOR)
    if originalImage is None:
        print 'Error: Unable to open Input image.'
        exit(-1)
    
    # mask File Name
    maskName = sys.argv[2]
    inpaintMask = cv2.imread(maskName, cv2.IMREAD_GRAYSCALE)
    if inpaintMask is None:
        print 'Error: Unable to open Mask image.'
        exit(-1)
    
    i = Inpainter(originalImage, inpaintMask, halfPatchWidth)
    check = i.checkValidInputs()
    if check == i.CHECK_VALID:
        i.inpaint()
        resultName = sys.argv[3]
        cv2.imwrite(resultName, i.result)
        # cv2.namedWindow("result")
        # cv2.imshow("result", i.result)
        # cv2.waitKey()
    else:
        print 'Error: invalid parameters (type %d).\n'%(check)
    
