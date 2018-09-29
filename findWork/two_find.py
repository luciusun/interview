#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 二分查找算法
'''

__author__ = 'slucius'


def findTwo(alist, value):
    if len(alist) < 0 or not alist:
        return False

    midIndex = len(alist) // 2
    if value == alist[midIndex]:
        return True
    elif value < alist[midIndex]:
        return findTwo(alist[:midIndex], value)
    else:
        return findTwo(alist[midIndex+1:], value)


def binarySearch(alist, value):
    if not value:
        return -1
    left = 0
    right = len(alist) - 1
    # if alist[-1] == value:
    #     return right
    # if alist[0] == value:
    #     return 0

    while left <= right:
        mid = (left+right) // 2
        if alist[mid] < value:
            left = mid + 1
        elif alist[mid] > value:
            right = mid - 1
        else:
            return mid

    return -1

print(binarySearch([1,2,3,4,5,6,7], 3))