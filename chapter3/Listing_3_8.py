1	import cv2
2	import numpy as np
3
4	# create a circle
5	circle = cv2.circle(np.zeros((200, 200, 3), dtype = "uint8"), (100,100), 90, (255,255,255), -1)
6	cv2.imshow("A white circle", circle)
7	cv2.waitKey(0)
8
9	# create a square
10	square = cv2.rectangle(np.zeros((200,200,3), dtype= "uint8"), (30,30), (170,170),(255,255,255), -1)
11	cv2.imshow("A white square", square)
12	cv2.waitKey(0)
13
14	#bitwise AND
15	bitwiseAnd = cv2.bitwise_and(square, circle)
16	cv2.imshow("AND Operation", bitwiseAnd)
17	cv2.waitKey(0)
18
19	#bitwise OR
20	bitwiseOr = cv2.bitwise_or(square, circle)
21	cv2.imshow("OR Operation", bitwiseOr)
22	cv2.waitKey(0)
23
24	#bitwise XOR
25	bitwiseXor = cv2.bitwise_xor(square, circle)
26	cv2.imshow("XOR Operation", bitwiseXor)
27	cv2.waitKey(0)
28
29	#bitwise NOT
30	bitwiseNot = cv2.bitwise_not(square)
31	cv2.imshow("NOT Operation", bitwiseNot)
32	cv2.waitKey(0)
