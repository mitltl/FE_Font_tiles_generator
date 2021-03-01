import cv2
for i in range(0,719):
	for j in range(0,10):
		picx = cv2.imread("%d,%d.png"%(i+1,j+2))
		print("%d,%d.png"%(i+1,j+2))
		for k in range(0,16):
			for l in range(0,15):
				if (picx[k,l] == [40,40,40]).all() and (picx[k,l+1] =  = [224,224,224]).all():
					picx[k,l+1] = [167, 168, 168]
		#picx = cv2.cvtColor(picx,cv2.COLOR_BGR2GRAY)#8位灰色
		cv2.imwrite("%d,%d.png" %(i+1,j+2),picx)

