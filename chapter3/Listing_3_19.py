1	import cv2
2	import numpy as np
3	# Load an image
4	image = cv2.imread("images/sudoku.jpg")
5	cv2.imshow("Original Image", image)
6	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
7	image = cv2.bilateralFilter(image, 5, 50, 50)
8	cv2.imshow("Blurred image", image)
9
10	# Sobel gradient detection
11	sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
12	sobelx = np.uint8(np.absolute(sobelx))
13	sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
14	sobely = np.uint8(np.absolute(sobely))
15
16	cv2.imshow("Sobel X", sobelx)
17	cv2.imshow("Sobel Y", sobely)
18
19	# Schar gradient detection by passing ksize = -1 to Sobel function
20	scharx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=-1)
21	scharx = np.uint8(np.absolute(scharx))
22	schary = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=-1)
23	schary = np.uint8(np.absolute(schary))
24	cv2.imshow("Schar X", scharx)
25	cv2.imshow("Schar Y", schary)
26
27	cv2.waitKey(0)
