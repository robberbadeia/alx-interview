#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    Function implementation
    """
    if not boxes:
        return False

    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
