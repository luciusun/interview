#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: some排序算法
'''

__author__ = 'slucius'



# 快速排序,O(nlogn)
def quicksort(alist, left, right):
    if left < right:
        pivotLocation = partition(alist, left, right)
        quicksort(alist, left, pivotLocation-1)
        quicksort(alist, pivotLocation+1, right)

def partition(alist, left, right):
    mid = (left+right) // 2
    pivot = alist[mid]
    swap(alist, right, mid)

    boundary = left
    for i in range(left, right):
        if alist[i] < pivot:
            swap(alist, boundary, i)
            boundary += 1
    swap(alist, boundary, right)
    return boundary



def swap(alist, i, j):
    alist[i], alist[j] = alist[j], alist[i]


# alist = [2, 9, 10, 4, 3, 6]
# quicksort(alist, 0, len(alist)-1)
# print(alist)




#归并排序,O(nlogn),采用分治法,且各层分治递归可以同时进行。

def mergeSort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])

    return merge(left, right)


def merge(left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

alist = [2, 9, 10, 4, 3, 6]
print(mergeSort(alist))



