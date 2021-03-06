﻿import cv2
import os
import numpy as np
picx = cv2.imread(input("位图路径？(*.bmp)"))
size = picx.shape
A = np.zeros((16,16,3),dtype = np.uint8)
#A = cv2.imread("template.png")
for i in range(0,int(size[0]/16)):
	for j in range(0,int(size[1]/16)):
		for k in range(0,16):
			for l in range(0,16):
				if (picx[16*i+k,16*j+l] == [0,0,0]).all():
					A[k,l] = [224,224,224]
				else:
					A[k,l] = [40,40,40]
		cv2.imwrite("%d,%d.png" %(i+1,j+2),A)
for i in range(0,int(size[0]/16)):
    for j in range(0,int(size[1]/16)):
        B  =  cv2.imread("%d,%d.png" %(i+1,j+2))        
        flagA = 0
        for x in range(0,16):
            for y in range(0,16):
                if (B[x,y] == [224,224,224]).all():
                    flagA+= 1
        if flagA == 256:
            print("正在移除%d,%d.png" %(i+1,j+2))
            os.remove("%d,%d.png" %(i+1,j+2))
