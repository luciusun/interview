#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'



def indexOfMin(lyst):
    '''Returns the index of the minimum item.
    O(n): time complexity.
    '''
    minIndex = 0
    curentIndex = 1
    while curentIndex < len(lyst):
        if lyst[curentIndex] < lyst[minIndex]:
            minIndex = curentIndex
        curentIndex += 1
    return minIndex


def indexOfMin_3_3_1(lyst):
    '''Returns the index of the minimum item.'''
    valMin = lyst[0]
    index = 0
    for i in range(1, len(lyst)):
        if lyst[i] < valMin:
            valMin = lyst[i]
            index = i

    return index, valMin

# print(indexOfMin([19,4,1,2,1,8,9,10,3]))

def sequentialSearch_3_3_2(target, lyst):
    '''Returns the position of the target item if found, or -1 otherwise .'''
    for i in range(len(lyst)):
        if target == lyst[i]:
            return i
    return -1

def sequentialSearch(target, lyst):
    '''Returns the position of the target item if found, or -1 otherwise .'''
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1

# print(sequentialSearch(3, [19,4,1,2,1,8,9,10,3]))


def binarySearch_3_3_4(target, sortedLyst):
    left = 0
    right = len(sortedLyst)-1
    while left < right:
        mid = (left + right) // 2
        if sortedLyst[mid] == target:
            return mid
        elif sortedLyst[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

# print(binarySearch_3_3_4(11, [1,2,3,4,5,6,7,8,9,10]))



class SavingsAccount(object):
    '''This class represents a savings account with the oener's name, PIN, and balance'''

    def __init__(self, name, pin, balance = 0.0):
        self._name = name
        self._pin = pin
        self._balance = balance


    def __lt__(self, other):
        return self._name < other._name

