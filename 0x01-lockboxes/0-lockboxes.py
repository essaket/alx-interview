#!/usr/bin/python3
'''Check if all boxes can be unlocked.'''

def canUnlockAll(boxes):
    '''Return True if all boxes can be unlocked.'''
    n = len(boxes)  # Total number of boxes
    seen = set([0])  # Set of unlocked boxes
    to_check = set(boxes[0])  # Keys from the first box

    while to_check:
        box = to_check.pop()  # Get a key
        if 0 <= box < n and box not in seen:
            seen.add(box)  # Mark box as seen
            to_check.update(boxes[box])  # Add new keys

    return len(seen) == n  # Check if all boxes are unlocked
