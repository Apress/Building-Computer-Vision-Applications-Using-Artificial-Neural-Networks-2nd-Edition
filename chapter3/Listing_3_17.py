1	import cv2
2	import numpy as np
3
4	# Load an image
5	image = cv2.imread("images/boat.jpg")
6	# convert the image to grayscale
7	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
8
9	cv2.imshow("Original Grayscale Image", image)
10
11	# Binarization using adaptive thresholding and simple mean
12	binarized = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 3)
13	cv2.imshow("Binarized Image with Simple Mean", binarized)
14
15	# Binarization using adaptive thresholding and Gaussian Mean
16	binarized = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
17	cv2.imshow("Binarized Image with Gaussian Mean", binarized)
18
19	cv2.waitKey(0)
