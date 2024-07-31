#!/usr/bin/python3
'''A module for working with lockboxes.'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first box
    is unlocked.
    '''
    n = len(boxes)  # Total number of boxes
    seen_boxes = set([0])  # Set keep track of unlocked boxes starting with 0
    unseen_boxes = set(boxes[0]).difference(set([0]))  # Keys from first box

    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()  # Get a key from unseen_boxes
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue  # Skip invalid indices
        if boxIdx not in seen_boxes:
            # Add keys from the current box to unseen_boxes and mark it as seen
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)

    # Return True if all boxes are seen (unlocked), otherwise False
    return n == len(seen_boxes)
