1	import cv2
2	import numpy as np
3
4	# Load an image
5	image = cv2.imread("images/scanned_doc.png")
6	# convert the image to grayscale
7	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
8	cv2.imshow("Original Grayscale Receipt", image)
9
10	# Binarize the image using thresholding
11	(T, binarizedImage) = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
12	cv2.imshow("Binarized Receipt", binarizedImage)
13
14	# Binarization with inverse thresholding
15	(Ti, inverseBinarizedImage) = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY_INV)
16	cv2.imshow("Inverse Binarized Receipt", inverseBinarizedImage)
17	cv2.waitKey(0)
