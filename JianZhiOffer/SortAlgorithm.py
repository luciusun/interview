#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 一些常见排序算法及其复杂度
'''

__author__ = 'slucius'

#冒泡排序
def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 0
        while i < n-1:
            if lyst[i] > lyst[i+1]:
                lyst[i], lyst[i+1] = lyst[i+1], lyst[i]
                swapped = True
            i += 1
        if not swapped:
            return lyst
        n -= 1
    return lyst




#选择排序
def selectSort(lyst):
    if not lyst or len(lyst) <= 0:
        return None
    for i in range(len(lyst)):
        for j in range(i+1, len(lyst)):
            if lyst[i] > lyst[j]:
                lyst[i], lyst[j] = lyst[j], lyst[i]

    return lyst






'''
堆排序.
一种选择排序，其时间复杂度为O(nlogn).
若在输出堆顶的最小值之后，使得剩余n-1个元素的序列重又建成一个堆，则得到n个元素的次小值。如此反复执行，便能得到一个有序序列，这个过程称之为堆排序。
'''

def heapSort(alist):
    if alist == None or len(alist) == 0:
        return None
    length = len(alist)
    output = []
    for i in range(length):
        tempLen = len(alist)
        for j in range(tempLen//2 - 1, -1, -1):
            preIndex = j
            preVal, heap = alist[preIndex], False
            while 2*preIndex < tempLen - 1 and not heap:
                curIndex = 2*preIndex + 1
                if curIndex < tempLen - 1:
                    if alist[curIndex] < alist[curIndex + 1]:
                        curIndex += 1
                if preVal >= alist[curIndex]:
                    heap = True
                else:
                    alist[preIndex] = alist[curIndex]
                    preIndex = curIndex
            alist[preIndex] = preVal
        output.insert(0, alist.pop(0))
    return output



print(heapSort([4,3,10,6,20]))







