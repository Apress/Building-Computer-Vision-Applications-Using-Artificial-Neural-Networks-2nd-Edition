1	import cv2
2	import numpy as np
3
4	# Load an image
5	image = cv2.imread("images/sudoku.jpg")
6	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
7	cv2.imshow("Blurred image", image)
8
9	# Binarize the image
10	(T,binarized) = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
11	cv2.imshow("Binarized image", binarized)
12
13	# Canny function for edge detection
14	canny = cv2.Canny(binarized, 0, 255)
15	cv2.imshow("Canny Edges", canny)
16
17	(contours, hierarchy) = cv2.findContours(canny,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
18	print("Number of contours determined are ", format(len(contours)))
19
20	copiedImage = image.copy()
21	cv2.drawContours(copiedImage, contours, -1, (0,255,0), 2)
22	cv2.imshow("Contours", copiedImage)
23	cv2.waitKey(0)
