#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note:
面试题33：把数组排成最小数:
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

__author__ = 'slucius'


# from functools import cmp_to_key
#
# class Solution:
#     def PrintMinNumber(self, numbers):
#         if numbers == None or len(numbers) <= 0:
#             return ''
#         strList = []
#         for i in numbers:
#             strList.append(str(i))
#
#         key = cmp_to_key(lambda x,y : int(x+y)-int(x-y))
#         strList.sort(key=key)
#         return ''.join(strList)



def PrintMinNumber(numbers):
    if numbers == None or len(numbers) <= 0:
        return ''
    strNum = [str(i) for i in numbers]
    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
                strNum[i], strNum[j] = strNum[j], strNum[i]
    print(strNum)
    return ''.join(strNum)

print(PrintMinNumber([3,32,321]))
