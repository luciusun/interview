#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

__author__ = 'slucius'


def Power(base, exponent):
    if(exponent == 0):
        return 1
    if(exponent == 1):
        return base
    if(exponent == -1):
        return 1.0/base

    '''
    当n为偶数, a^n = a^(n/2) * a^(n/2)
    当n为奇数, a^n = a^((n-1)/2) * a^((n-1)/2)) * a
    利用右移一位运算代替除以2
    利用位与运算代替了求余运算法%来判断一个数是奇数还是偶数
    优化代码速度
    '''
    result = Power(base, exponent>>1)
    result *= result
    if (exponent & 0x1)==1:
        result = result*base
    return result


print(Power(2, 3))