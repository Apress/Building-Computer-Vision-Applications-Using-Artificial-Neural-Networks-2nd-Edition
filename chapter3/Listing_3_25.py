1	import cv2
2	import numpy as np
3	# load the input image and template image from disk
4	image = cv2.imread("images/pepsico.png")
5	template = cv2.imread("images/pepsi.png")
6	# Resize the template so that the dimenions are less than the image dimenions
7	template = cv2.resize(template, None, fx=0.5, fy=0.5)
8	#Get the height and width of the template
9	(tH, tW) = template.shape[:2]
10	# convert both the image and template to grayscale
11	imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
12	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
13	# perform template matching
14	result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
15	# find all locations in the result where the matched value is
16	# greater than the threshold
17	(yCoords, xCoords) = np.where(result >= 0.5)
18	#clone the original image so we can draw rectangular regions on it.
19	clone = image.copy()
20	# loop over our starting (x, y)-coordinates
21	for (x, y) in zip(xCoords, yCoords):
22		# draw the bounding box on the image
23		cv2.rectangle(clone, (x, y), (x + tW, y + tH),
24			(0, 255, 255), 2)
25	# show our output image without applying non_max_suppression of overlapping bounding boxes
26	cv2.imshow("Without NMS", clone)
27	# Let us now apply NMS
28	# initialize our list of rectangles
29	rects = []
30	# loop over the starting (x, y)-coordinates again
31	for (x, y) in zip(xCoords, yCoords):
32		# update the list of rectangles
33		rects.append((x, y, x + tW, y + tH))
34	#We gave equal scores to all bounding boxes
35	pick = non_max_suppression(np.array(rects),  np.ones(len(rects)), 0.7)
36	# loop over the final bounding boxes
37	for (startX, startY, endX, endY) in pick:
38		# draw the bounding box on the image
39		cv2.rectangle(image, (startX, startY), (endX, endY),
40			(255, 0, 255), 2)
41	# show the output image
42	cv2.imshow("After NMS", image)
43	cv2.waitKey(0)
