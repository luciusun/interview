#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


def xunHuanNumber(x, y):
    # m = x//y
    # n = x%y
    loopDict = {}
    numList = []
    cnt = 0
    while(True):
        numList.append(x//y)
        cnt += 1
        x = 10 * (x % y)
        # n = 10 * n % y
        if x==0:
            break
        flag = loopDict.get(x)
        if flag:
            print(l)
            break
        loopDict[x] = cnt
