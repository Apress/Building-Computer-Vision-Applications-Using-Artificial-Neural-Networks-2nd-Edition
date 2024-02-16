1	#Example to demonstrate image flipping in various directions
2	import cv2
3	import numpy as np
4
5	# Load image
6	imagePath = "images/zebrasmall.png"
7	image = cv2.imread(imagePath)
8
9	# Flip horizontally
10	flippedHorizontally = cv2.flip(image, 1)
11	cv2.imshow("Flipped Horizontally", flippedHorizontally)
12	cv2.waitKey(-1)
13
14	# Flip vertically
15	flippedVertically = cv2.flip(image, 0)
16	cv2.imshow("Flipped Vertically", flippedVertically)
17	cv2.waitKey(-1)
18	# Flip horizontally and then vertically
19	flippedHV = cv2.flip(image, -1)
20	cv2.imshow("Flipped H and V", flippedHV)
21	cv2.waitKey(0)
