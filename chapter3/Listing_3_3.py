1	#Example code to demonstrate image rotation using OpenCV’s warpAffine function
2	import cv2
3	import numpy as np
4
5	# Load image
6	imagePath = "images/zebrasmall.png"
7	image = cv2.imread(imagePath)
8	(h,w) = image.shape[:2]
9
10	#Define translation matrix
11	center = (h//2, w//2)
12	angle = -45
13	scale = 1.0
14
15	rotationMatrix = cv2.getRotationMatrix2D(center, angle, scale)
16
17	# Rotate the image
18	rotatedImage = cv2.warpAffine(image, rotationMatrix, (image.shape[1], image.shape[0]))
19
20	cv2.imshow("Rotated image", rotatedImage)
21	cv2.waitKey(0)
