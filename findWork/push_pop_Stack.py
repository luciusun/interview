#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 判断入栈顺序和出栈顺序是否合理.
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
(注意：这两个序列的长度是相等的）

'''

__author__ = 'slucius'

#
def is_pop_order(pushV, popV):
    if len(pushV) == 0:
        return False

    stack = []
    j = 0
    for i in range(len(pushV)):
        stack.append(pushV[i])
        while  stack[-1] == popV[j] and j < len(popV):
            stack.pop()
            j += 1

            #必须加这一行，否则当stack提前为空时，进入循环后，list索引错误.
            if len(stack) == 0:
                break

    if len(stack) == 0:
        return True
    else:
        return False





print(is_pop_order([1,2,3,4,5], [4,3,5,1,2]))