1	#Image transformation using the resize() function
2	import cv2
3	import numpy as np
4
5	# Load image
6	imagePath = "images/zebra.png"
7	image = cv2.imread(imagePath)
8
9	# Get image shape which returns height, width, and channels as a tuple. Calculate the aspect ratio
10	(h, w) = image.shape[:2]
11	aspect = w / h
12
13	# lets resize the image to  decrease height by half of the original image.
14	# Remember, pixel values must be integers.
15	height = int(0.5 * h)
16	width =  int(height * aspect)
17
18	# New image dimension as a tuple
19	dimension = (height, width)
20	resizedImage = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA)
21	cv2.imshow("Resized Image", resizedImage)
22
23	# Resize using x and y factors
24	resizedWithFactors = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_LANCZOS4)
25	cv2.imshow("Resized with factors", resizedWithFactors)
26	cv2.waitKey(0)
