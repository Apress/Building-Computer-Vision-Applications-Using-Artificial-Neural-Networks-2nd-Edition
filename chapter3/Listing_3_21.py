1	import cv2
2	import numpy as np
3
4	# Load an image
5	image = cv2.imread("images/sudoku.jpg")
6	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
7	cv2.imshow("Blurred image", image)
8
9	# Canny function for edge detection
10	canny = cv2.Canny(image, 50, 170)
11	cv2.imshow("Canny Edges", canny)
12
13	cv2.waitKey(0)
