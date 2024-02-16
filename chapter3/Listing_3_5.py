1	#Example to demonstrate image cropping
2	import cv2
3	import numpy as np
4
5	# Load image
6	imagePath = "images/zebrasmall.png"
7	image = cv2.imread(imagePath)
8	cv2.imshow("Original Image", image)
9	cv2.waitKey(0)
10
11	# Crop the image to get only the face of the zebra
12	croppedImage = image[0:150, 0:250]
13	cv2.imshow("Cropped Image", croppedImage)
14	cv2.waitKey(0)
