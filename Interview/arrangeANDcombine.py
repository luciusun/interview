#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'slucius'



#排列算法 and 组合算法


def fullArange(alist, stack):
    #定义了两个列表，一个列表存的是需要全排列的数据，另一个列表是当做栈来用的，可以把这个递归想成一棵树
    if not alist:
        print(stack)

    else:
        for i in range(len(alist)):
            stack.append(alist[i])
            del alist[i]
            fullArange(alist, stack)

            alist.insert(i, stack.pop())



alist = [1,2,3]
stack = []
fullArange(alist,stack)




COUNT = 0
def fullArange1(alist, begin, end):
    global COUNT

    if begin >= end:
        print(alist)
        COUNT += 1

    else:
        i = begin
        for num in range(begin, end):
            alist[num], alist[i] = alist[i], alist[num]
            fullArange1(alist, begin+1, end)
            alist[num], alist[i] = alist[i], alist[num]

alist1 = [1,2,3]
fullArange1(alist1,0,len(alist1))
print(COUNT)









