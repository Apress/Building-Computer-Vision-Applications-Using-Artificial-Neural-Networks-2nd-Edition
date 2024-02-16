1	import cv2
2	import numpy as np
3
4	# Load the image
5	natureImage = cv2.imread("images/nature.jpg")
6
7	# Split the image into component colors
8	(b,g,r) = cv2.split(natureImage)
9
10	# show the blue image
11	cv2.imshow("Blue Image", b)
12
13	# Show the green image
14	cv2.imshow("Green image", g)
15
16	# Show the red image
17	cv2.imshow("Red image", r)
18	cv2.waitKey(0)
