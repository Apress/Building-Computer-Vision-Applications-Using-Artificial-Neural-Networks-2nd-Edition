1	import cv2
2
3	target = cv2.imread('images/obama_with_people.jpg', cv2.IMREAD_GRAYSCALE)
4
5	template = cv2.imread('images/obama_face.jpg', cv2.IMREAD_GRAYSCALE)
6	#Resize the template so that the dimensions of template is smaller than the target's
7	template = cv2.resize(template, None, fx=0.2, fy=0.2)
8
9	w, h = template.shape[::-1]
10	# All 6 suported comparison methods
11	methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
12	            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
13	for m in methods:
14	    img = target.copy()
15	    method = eval(m)
16	    # Apply template Matching
17	    result = cv2.matchTemplate(img, template, method)
18	    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
19	    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum, else take maximum
20	    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
21	        top_left = min_loc
22	    else:
23	        top_left = max_loc
24	    bottom_right = (top_left[0] + w, top_left[1] + h)
25	    cv2.rectangle(img,top_left, bottom_right, 255, 2)
26	    cv2.imshow(m, img)
27	    cv2.waitKey(0)
28
29	cv2.destroyAllWindows()
