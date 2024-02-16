1	#Example program to demonstrate two approaches of adding images
2	import cv2
3	import numpy as np
4
5	image1Path = "images/zebra.png"
6	image2Path = "images/nature.jpg"
7
8	image1 = cv2.imread(image1Path)
9	image2 = cv2.imread(image2Path)
10
11	# resize the two images to make them of the same dimension. This is a must to add two images
12	resizedImage1 = cv2.resize(image1,(300,300),interpolation=cv2.INTER_AREA)
13	resizedImage2 = cv2.resize(image2,(300,300),interpolation=cv2.INTER_AREA)
14
15	# This is a simple addition of two images
16	resultant = cv2.add(resizedImage1, resizedImage2)
17
18	# Display these images to see the difference
19	cv2.imshow("Resized 1", resizedImage1)
20	cv2.waitKey(0)
21
22	cv2.imshow("Resized 2", resizedImage2)
23	cv2.waitKey(0)
24
25	cv2.imshow("Resultant Image", resultant)
26	cv2.waitKey(0)
27
28	# This is weighted addition of the two images
29	weightedImage = cv2.addWeighted(resizedImage1,0.7, resizedImage2, 0.3, 0)
30	cv2.imshow("Weighted Image", weightedImage)
31	cv2.waitKey(0)
32
33	imageEnhanced = 255*resizedImage1
34	cv2.imshow("Enhanced Image", imageEnhanced)
35	cv2.waitKey(0)
36
37	arrayImage = resizedImage1+resizedImage2
38	cv2.imshow("Array Image", arrayImage)
39	cv2.waitKey(0)
