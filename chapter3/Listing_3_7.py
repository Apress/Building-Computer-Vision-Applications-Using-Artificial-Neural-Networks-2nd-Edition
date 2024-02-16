1	import cv2
2	import numpy as np
3
4
5	image1Path = "images/cat1.png"
6	image2Path = "images/cat2.png"
7
8	image1 = cv2.imread(image1Path)
9	image2 = cv2.imread(image2Path)
10
11	# resize the two images to make them of the same dimensions. This is a must to subtract two images
12	resizedImage1 = cv2.resize(image1,(int(500*image1.shape[1]/image1.shape[0]), 500),interpolation=cv2.INTER_AREA)
13	resizedImage2 = cv2.resize(image2,(int(500*image2.shape[1]/image2.shape[0]), 500),interpolation=cv2.INTER_AREA)
14
15	cv2.imshow("Cat 1", resizedImage1)
16	cv2.imshow("Cat 2", resizedImage2)
17
18	# Subtract image 1 from 2
19	cv2.imshow("Diff Cat1 and Cat2",cv2.subtract(resizedImage2, resizedImage1))
20	cv2.waitKey(0)
21
22
23	# subtract images 2 from 1
24	subtractedImage = cv2.subtract(resizedImage1, resizedImage2)
25	cv2.imshow("Cat2 subtracted from Cat1", subtractedImage)
26	cv2.waitKey(0)
27
28	# Numpy Subtraction Cat2 from Cat1
29	subtractedImage2 = resizedImage2 - resizedImage1
30	cv2.imshow("Numpy Subracts Images", subtractedImage2)
31	cv2.waitKey(0)
32
33	# A constant subtraction
34	subtractedImage3 = resizedImage1 - 50
35	cv2.imshow("Constant Subtracted from the image", subtractedImage3)
36	cv2.waitKey(0)
