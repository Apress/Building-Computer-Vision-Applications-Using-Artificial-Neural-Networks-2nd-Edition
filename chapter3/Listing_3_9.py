1	import cv2
2	import numpy as np
3
4	# Load an image
5	natureImage = cv2.imread("images/nature.jpg")
6	cv2.imshow("Original Nature Image", natureImage)
7
8	# Create a rectangular mask
9	maskImage = cv2.rectangle(np.zeros(natureImage.shape[:2], dtype="uint8"),
10	                     (50, 50), (int(natureImage.shape[1])-50, int(natureImage.shape[0] / 2)-50), (255, 255, 255), -1)
11	cv2.imshow("Mask Image", maskImage)
12	cv2.waitKey(0)
13
14	# Using bitwise_and operation perform masking. Notice the mask=maskImage argument
15	masked = cv2.bitwise_and(natureImage, natureImage, mask=maskImage)
16	cv2.imshow("Masked image", masked)
17	cv2.waitKey(0)
