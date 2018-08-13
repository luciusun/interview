#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note:
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

__author__ = 'slucius'



def reOrderArray(array):
    i = list(filter(lambda x: (x+1)%2==0, array))
    j = list(filter(lambda x:  x%2==0, array))
    return (i+j)

#直接利用Python的trick, 写一个简单的排列数组, 顺序不变
# left = [x for x in array if x&1]
# right = [x for x in array if not x&1]
# print(reOrderArray([1,2,3,4,5,6,7,8,9,10]))


#一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变
def reOrderArray1(array):
    if len(array)<1:
        return
    elif len(array)==1:
        return array


    first = 0
    last = len(array) - 1
    while(first <= last):
        # while (array[first])%2:
        while array[first] & 0x1 == 1:
            first += 1
        # while (array[last-1])%2:
        while array[last] & 0x1 == 0:
            last -= 1
        array[first], array[last] = array[last], array[first]
    array[first], array[last] = array[last], array[first]
    return array

print(reOrderArray1([1,2,3,4,5,6,7,8,9,10]))