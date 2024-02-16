1	import cv2
2
3	# Load a noisy image
4	noisyImage = cv2.imread("images/nature.jpg")
5	cv2.imshow("Original image", noisyImage)
6
7	# Bilateral Filter with
8	fileteredImag5 = cv2.bilateralFilter(noisyImage, 5, 150,50)
9	cv2.imshow("Blurred image 5", fileteredImag5)
10
11	# Bilateral blurring with kernal 7
12	fileteredImag7 = cv2.bilateralFilter(noisyImage, 7, 160,60)
13	cv2.imshow("Blurred image 7", fileteredImag7)
14
15	cv2.waitKey(0)
