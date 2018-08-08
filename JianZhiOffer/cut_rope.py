#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


def cut_rope(length):
    l = [0, 1, 2, 3]
    if(length==0):
        return 0
    if(length==1):
        return 1
    if(length==2):
        return 1
    if(length==3):
        return 2
    for j in range(4,length+1):
        valMax = 0
        for i in range(1,j//2+1):
            temp = l[i] * l[j-i]
            if(temp>valMax):
                valMax = temp
        l.append(valMax)
    return l[-1]


for i in range(10):
    print(cut_rope(i))