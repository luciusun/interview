#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'



#

#def fibonacci(n):
#     if (n == 0):
#         return 0
#     if (n == 1):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
#
#
# for i in range(10):
#
#     print(fibonacci(i))
#
#
# class Solution(object):
#     def fib(self, n):
#         if(n==0):
#             return 0
#         if(n==1):
#             return 1
#         return self.fib(n-1)+self.fib(n-2)
#
# s=Solution()
# print(s.fib(3))




def fibonacci1(n):
    temp = [0, 1]
    if (n < 2):
        return temp[n]
    fibZero = 0
    fibOne = 1
    # fibN = 0
    i = 1
    while (i < n):
        fibN = fibZero + fibOne
        fibOne, fibZero = fibN, fibOne
        i = i + 1
    return fibN

for i in range(10):

    print(fibonacci1(i))

print('................................')


def fibonacci2(n):
    temp = [0, 1]
    if(n>=2):
        for i in range(2, n+1):
            temp[i%2] = temp[0] + temp[1]
        return temp[n%2]

for i in range(10):

    print(fibonacci2(i))




def jump(n):
    temp = [1, 2]
    if(n>=3):
        for i in range(3, n+1):
            temp[(i+1)%2] = temp[0] + temp[1]
        return temp[(n+1)%2]
