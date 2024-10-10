#!/usr/bin/python3
""" Moudule """


def canUnlockAll(boxes):
    """ Function """
    if type(boxes) is not list:
        return False
    if len(boxes) == 0:
        return False
    for i in range(1, len(boxes)):
        isTr = False
        for j in range(len(boxes)):
            if i in boxes[j] and i != j:
                isTr = True
                break
        if isTr is False:
            return False
    return True
