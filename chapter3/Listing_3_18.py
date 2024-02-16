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
11	(T, binarizedImage) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
12	print("Threshold value with Otsu binarization", T)
13	cv2.imshow("Binarized Receipt", binarizedImage)
14
15	# Binarization with inverse thresholding
16	(Ti, inverseBinarizedImage) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
17	cv2.imshow("Inverse Binarized Receipt", inverseBinarizedImage)
18	print("Threshold value with Otsu inverse binazarion", Ti)
19	cv2.waitKey(0)
