import cv2
import os
import numpy as np
for i in range(0,719):
    for j in range(0,10):
        B  =  cv2.imread("%d,%d.png" %(i+1,j+2))        
        flagA = 0
        for x in range(0,16):
            for y in range(0,8):
                if (B[x,y+8] == [224,224,224]).all():
                    flagA+= 1
        if flagA == 128:
            print("%d,%d.png" %(i+1,j+2))
            os.remove("%d,%d.png" %(i+1,j+2))
#os.system('for file in $(ls); do magick $file PNG:$file; done') #linux下用，现在不是必要的了
