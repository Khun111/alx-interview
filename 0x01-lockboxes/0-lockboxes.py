#!/usr/bin/python3
'''Module for lockboxes'''
from collections import deque


def canUnlockAll(boxes):
    '''Function for lockboxes'''
    num_boxes = len(boxes)
    visited = set()
    queue = deque([0])  # Start with box 0
    visited.add(0)

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key < num_boxes and key not in visited:
                queue.append(key)
                visited.add(key)

    return len(visited) == num_boxes
