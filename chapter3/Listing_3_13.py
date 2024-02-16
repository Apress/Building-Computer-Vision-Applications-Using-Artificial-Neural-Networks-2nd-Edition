1	import cv2
2	import numpy as np
3
4	# Load the park image
5	parkImage = cv2.imread("images/park.jpg")
6	cv2.imshow("Original Image", parkImage)
7
8	# Gaussian blurring with 3x3 kernel height and 0 for standard deviation to calculate from the kernel
9	GaussianFiltered = cv2.GaussianBlur(parkImage, (5,5), 0)
10	cv2.imshow("Gaussian Blurred Image", GaussianFiltered)
11
12	cv2.waitKey(0)
