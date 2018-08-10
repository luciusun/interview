#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitPoint-1)
        quickSortHelper(alist, splitPoint+1, last)

def partition(alist, first, last):
    pivotvlue = alist[first]

    leftmark = first+1
    rightmark = last
    done = False

    while not done:
        while alist[leftmark] <= pivotvlue and leftmark <= rightmark:
            leftmark += 1
        while alist[rightmark] >= pivotvlue and rightmark >= leftmark:
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark
#
# alist = [54,26,93,17,77,31,44,55,20]
# # alist2 = [1]
# quickSort(alist)
# print(alist)



def bubbleSort(alist):
    for j in range(1, len(alist)-1):
        for i in range(len(alist)-j):
            if(alist[i] > alist[i+1]):
                alist[i+1], alist[i] = alist[i], alist[i+1]
                print(alist)


l = [54,26,93,17,77,31,44,55,20,5,22,56,12]
# bubbleSort(l)


def merge(a, b):
    c = list()
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i==len(a):
        for k in b[j:]:
            c.append(k)


    if j==len(b):
        for k in a[i:]:
            c.append(k)

    return c



def mergeSort(alist):
    if len(alist)<=1:
        return alist

    mid = len(alist)//2
    left = mergeSort(alist[:mid])
    right = mergeSort(alist[mid:])
    return merge(left, right)


print(mergeSort(l))