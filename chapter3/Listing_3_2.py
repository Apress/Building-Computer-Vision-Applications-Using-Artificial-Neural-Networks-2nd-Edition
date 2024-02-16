1	#Image translation using OpenCV’s to move image along x and y-axes
2	import cv2
3	import numpy as np
4
5	#Load image
6	imagePath = "images/soccer-in-green.jpg"
7	image = cv2.imread(imagePath)
8
9	#Define translation matrix
10	translationMatrix = np.float32([[1,0,50],[0,1,20]])
11
12	#Move the image
13	movedImage = cv2.warpAffine(image, translationMatrix, (image.shape[1], image.shape[0]))
14
15	cv2.imshow("Moved image", movedImage)
16	cv2.waitKey(0)
