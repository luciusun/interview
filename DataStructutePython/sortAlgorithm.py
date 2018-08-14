#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'

def swap(lyst, i, j):
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def selectionSort_3_4_1(lyst):
    '''选择排序'''
    for i in range(len(lyst)):
        for j in range(i+1, len(lyst)):
            if lyst[j] < lyst[i]:
                swap(lyst, i, j)
    return lyst

    # position = 1
    # min = lyst[0]
    # while position < len(lyst):
    #     if lyst[position] < min:

# print(selectionSort([4, 10,100,99,40,7,5, 3, 1, 2, 4]))


def selectionSort(lyst):
    '''选择排序'''
    i = 0
    while i < len(lyst)-1:
        minIndex = i
        j = i+1
        while j < len(lyst):
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j = j + 1

        if minIndex != i:
            swap(lyst, minIndex, i)
        i += 1
    return lyst



def bubbleSort(lyst):
    '''冒泡排序'''
    # i = 1
    # maxIndex = 0
    # while i < len(lyst):
    #     if lyst[i] > lyst[maxIndex]:
    #         swap(lyst, i, maxIndex)
    #         maxIndex = i
    #     i += 1
    # return lyst
    n = len(lyst)

    while n>1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i-1]:
                swap(lyst, i, i-1)
                swapped = True
            i += 1
        if not swapped:
            print(1)
            return lyst
        n -= 1
    return lyst



# print(bubbleSort([1,2,3,4]))

def insertionSort(lyst):
    '''插入排序'''
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i-1
        while j>=0:
            if itemToInsert < lyst[j]:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = itemToInsert
        i += 1
    return lyst


# print(insertionSort([1,2,3,5,90,3,54]))



def quicksort_3_5_1(lyst):
    '''快速排序'''
    quicksortHelper(lyst, 0, len(lyst)-1)


def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation-1)
        quicksortHelper(lyst, pivotLocation + 1, right)


def partition(lyst, left, right):
    middle = (left+right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # pivot, lyst[right] = lyst[right], pivot
    #set the boundary point to first position.
    boundary = left
    for i in range(left, right):
        if lyst[i] < pivot:
            swap(lyst, i, boundary)
            boundary += 1
    swap(lyst, right, boundary)
    return boundary



alist=[1,2,3,5,90,3,54]
quicksort_3_5_1(alist)
print(alist)




















