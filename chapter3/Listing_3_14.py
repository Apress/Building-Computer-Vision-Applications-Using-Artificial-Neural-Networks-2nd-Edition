1	import cv2
2
3	# Load a noisy image
4	saltpepperImage = cv2.imread("images/salt-pepper.jpg")
5	cv2.imshow("Original noisy image", saltpepperImage)
6
7	# Median filtering for noise reduction
8	blurredImage3 = cv2.medianBlur(saltpepperImage, 3)
9	cv2.imshow("Blurred image 3", blurredImage3)
10
11	# Median filtering for noise reduction
12	blurredImage5 = cv2.medianBlur(saltpepperImage, 5)
13	cv2.imshow("Blurred image 5", blurredImage5)
14	cv2.waitKey(0)
