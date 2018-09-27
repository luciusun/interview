#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


def fn(n ,m, p, ln, lm):
    d = dict()
    for i in range(1, n+1):
        d[i] = ln[i-1]
    print(d)

    for j in lm:
        if j[0] == 'A':
            d[j[1]] += 1
        else:
            d[j[1]] -= 1

    # print(d[])
    print(d)

    sorted_d = sorted(d.items(), key = lambda item:item[1])
    sorted_d = sorted_d[::-1]
    print(sorted_d)
    for i in range(1, n+1):
        if p == sorted_d[i-1][0]:
            print(i)
            break


print(fn(3,4,1,[5,3,1],[('B',1),('A',2),('A',2),('A',3)]))
