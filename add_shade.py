import cv2
import os
for file in os.listdir("."):
    picx = cv2.imread(file)
    for k in range(0,16):
        for l in range(0,15):
            if (picx[k,l] == [167,168,168]).all() :
                picx[k,l+1] = [248, 248, 248]#火花狼组圣魔为字阴影为[167,168,168]
    cv2.imwrite(file,picx)

