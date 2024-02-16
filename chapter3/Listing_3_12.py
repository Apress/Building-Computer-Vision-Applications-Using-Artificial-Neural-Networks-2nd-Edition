1	import cv2
2	import numpy as np
3
4	# Load the image
5	park = cv2.imread("images/nature.jpg")
6	cv2.imshow("Original Park Image", park)
7
8	#Define the kernal
9	kernal = (3,3)
10	blurred3x3 = cv2.blur(park,kernal)
11	cv2.imshow("3x3 Blurred Image", blurred3x3)
12
13	blurred5x5 = cv2.blur(park,(5,5))
14	cv2.imshow("5x5 Blurred Image", blurred5x5)
15
16	blurred7x7 = cv2.blur(park, (7,7))
17	cv2.imshow("7x7 Blurred Image", blurred7x7)
18	cv2.waitKey(0)
