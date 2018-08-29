#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'

#方法一：暴力法

#方法二：两遍哈希表

def twoSum1(nums, target):
    d = {}
    for i, value in enumerate(nums):
        if value not in d:
            d[value] = i

    for i, value in enumerate(nums):
        diff = target - value
        if diff in d and i != d[diff]:
            return [i, d[diff]]

print(twoSum1([2,7,11,15], 9))

#方法三：一遍哈希表

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    my_dict = {}
    for i in range(len(nums)):
        index = nums[i]
        diff = target - index
        if diff in my_dict:
            return [i, my_dict[diff]]
        my_dict[index] = i