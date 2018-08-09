#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


def binary_one(n):
    '''
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
    :param n:
    :return:
    '''
    if(n<0):
        n = n&0xffffffff
    if(n==0):
        return 0
    i = 0
    while(True):
        n = n&(n-1)
        i = i+1
        if(n==0):
            return i

# print(binary_one(-5))



def powerOf2(n):
    '''
    判断一个数是不是2得整数次幂
    :param n:
    :return:
    '''
    if(n<0):
        return False
    if(n==0):
        return True
    if(n>0):
        if (n & (n - 1)==0):
            return True
        return False
print(powerOf2(1))


def andOr(m, n):
    '''
    判断两个数的二进制表示有多少位不一样, 直接比较两个数的二进制异或就可以
    :param m:
    :param n:
    :return:
    '''
    diff = m^n
    count = 0
    while diff:
        diff = diff&(diff-1)
        count = count+1
    return count

