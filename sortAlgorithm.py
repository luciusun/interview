#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: some排序算法
'''

__author__ = 'slucius'


# def quicksort(alist, left, right):
#     if left < right:
#         pivotLocation = partition(alist, left, right)
#         quicksort(alist, left, pivotLocation-1)
#         quicksort(alist, pivotLocation+1, right)
#
# def partition(alist, left, right):
#     mid = (left+right) // 2
#     #swap
#     pivot = alist[mid]
#     alist[mid] = alist[right]
#     alist[right] = pivot
#
#     #set boundary
#     boundary = left
#     for i in range(left, right):
#         if alist[i] < pivot:
#             swap(alist, i, boundary)
#             boundary += 1
#     swap(alist, right ,boundary)
#
#     return boundary
#
# def swap(alist, i, j):
#     alist[i], alist[j] = alist[j], alist[i]



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


alist = [2, 9, 10, 4, 3, 6]
quicksort(alist, 0, len(alist)-1)
print(alist)

