#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'document note: '

__author__ = 'slucius'


def median(lst):
    '''
    cacl median in a list.
    :param lst:
    :return:
    '''
    lst = sorted(lst)
    if len(lst) % 2 == 0:
        return lst[len(lst) // 2 - 1:len(lst) // 2 + 1]
    else:
        return lst[len(lst) // 2:len(lst) // 2 + 1]






def mode(lst):
    f = []
    s = set(lst)
    # return max(lst.count(x) for x in set(lst))
    for x in s:
        f.append(lst.count(x))
    i = f.index(max(f))
    # print(f)
    # print(s)
    # print(i)
    s1 = list(s)
    return s1[i]


#if have two equal max number, how to solve?
print(mode([1,3,2,1,5,8,5,6,7,8,8]))
# mode([1,3,2,1,5,8])


def mean(lst):
    return sum(lst)/len(lst)

print(mean([1,3,2,1,5,8]))
