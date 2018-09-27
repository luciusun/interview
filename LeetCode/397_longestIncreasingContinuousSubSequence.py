#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），
请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）
样例 :
给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.
给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.

思路

1. if a<=2:  return a
2. 先判断数组的第一个元素和第二个元素之间的关系是越来越大还是越来越小（此处定义为0 or 1),此处连续子序列已经至少有两个，即sum=2
3. 对后面的数组元素进行判断，满足一开始的关系（0 or 1)，sum+1,直到关系发生改变（0->1 or 1->0)，比较存放最大次数的comp和sum,将最大值放于sum.
4. 循环3，直到读取到最后一个元素
5. return comp


'''


__author__ = 'slucius'


class Solution():
    def findLongest(self, alist):
        if len(alist) <= 2:
            return len(alist)

        # incresing
        flag = 0
        if alist[0] > alist[1]:
            flag = 1

        sum = 2
        comp = 0
        for i in range(2, len(alist)):
            if alist[i] > alist[i-1] and flag == 0 or alist[i] < alist[i-1] and flag == 1:
                sum += 1

            if alist[i] > alist[i-1] and flag == 1 or alist[i] < alist[i-1] and flag == 0:
                if comp < sum:
                    comp = sum
                sum = 2

                flag = 0
                if alist[i] < alist[i-1]:
                    flag = 1

        if comp < sum:
            comp = sum
        return comp


s = Solution()
print(s.findLongest([5,1,2,3,4]))
