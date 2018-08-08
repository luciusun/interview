#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'document note: '

__author__ = 'slucius'



def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    while(first <= last):
        middle = (first + last) // 2
        if(item < alist[middle]):
            last = middle - 1
        elif(item > alist[middle]):
            first = middle + 1
        else:
            return middle
    return -1



test = [0,1,2,8,13,17,19,32,42]
print(binarySearch(test, 13))

