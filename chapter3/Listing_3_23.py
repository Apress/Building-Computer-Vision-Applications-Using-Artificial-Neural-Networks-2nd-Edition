1	import cv2
2	import numpy as np
3
4	# Load the image
5	image = cv2.imread("images/sudoku.jpg", 0)
6
7	# Define the structuring element
8	kernel = np.ones((5, 5), np.uint8)
9
10	# Perform erosion
11	erosion = cv2.erode(image, kernel, iterations=1)
12
13	# Perform dilation
14	dilation = cv2.dilate(image, kernel, iterations=1)
15
16	# Perform opening
17	opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
18
19	# Perform closing
20	closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
21
22	# Perform morphological gradient
23	gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
24
25	# Perform top hat
26	tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
27
28	# Perform black hat
29	blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
30
31	# Display the results
32	cv2.imshow("Original Image", image)
33	cv2.imshow("Erosion", erosion)
34	cv2.imshow("Dilation", dilation)
35	cv2.imshow("Opening", opening)
36	cv2.imshow("Closing", closing)
37	cv2.imshow("Morphological Gradient", gradient)
38	cv2.imshow("Top Hat", tophat)
39	cv2.imshow("Black Hat", blackhat)
40
41	# Wait for key press and exit
42	cv2.waitKey(0)
43	cv2.destroyAllWindows()
