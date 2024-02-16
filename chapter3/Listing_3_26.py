#The NMS function
def non_max_suppression(boxes, scores, overlap_threshold):
    # If there are no boxes, return an empty list
    if len(boxes) == 0:
        return []
    # Initialize the list of picked indices
    pick = []
    # Grab the coordinates of the bounding boxes
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    # Compute the area of the bounding boxes
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    # Sort the bounding boxes by their scores in descending order
    idxs = np.argsort(scores)
    # Keep looping while there are indices to be processed
    while len(idxs) > 0:
        # Grab the last index in the sorted list and add it to the list of
        # picked indices
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)
        # Find the largest (x, y) coordinates for the start of the bounding box
        # and the smallest (x, y) coordinates for the end of the bounding box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])
        # Compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)
        # Compute the overlap ratio
        overlap = (w * h) / area[idxs[:last]]
        # Delete all indices from the index list that have overlap greater
        # than the specified threshold
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlap_threshold)[0])))
    # Return only the bounding boxes that were picked
    return boxes[pick]
