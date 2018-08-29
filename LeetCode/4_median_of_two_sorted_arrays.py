#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 方法：递归法
'''

__author__ = 'slucius'


def findMedianNum(num1, num2):
    '''
    :param num1: list[int]
    :param num2: list[int]
    :return: float
    '''
    # if not num1 and not num2:
    #     return None
    m = len(num1)
    n = len(num2)
    # m = min(length1, length2)
    # n = max(length1, length2)
    if m > n:
        num1, num2, m, n = num2, num1, n, m

    if n == 0:
        return None
    imin, imax = 0, m

    while imin <= imax:
        i = (imin+imax)//2
        j = (m+n+1)//2 - i
        if i < m and num2[j-1] > num1[i]:
            imin = i+1
        elif i>0 and num1[i-1] > num2[j]:
            imax = i-1
        else:
            # i is perfect.
            if i == 0:
                max_of_left = num2[j-1]
            elif j == 0:
                max_of_left = num1[i-1]
            else:
                max_of_left = max(num1[i-1],num2[j-1])

            if (m+n)%2 == 1:
                return max_of_left

            if i == m:
                min_of_right = num2[j]
            elif j == n:
                min_of_right = num1[i]
            else:
                min_of_right = min(num1[i], num2[j])

            return (min_of_right + max_of_left) /2.0


print(findMedianNum([1,2,4],[2,3,5]))
