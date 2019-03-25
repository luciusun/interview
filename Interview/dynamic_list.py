#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'slucius'

'''
给定一个只含正数的数组，找到数组满足条件的元素的最大和，条件是：组成最大和的所有元素不能相邻;
比如数组 [3,2,7,10] 返回 13（3+10），数组 [3,2,5,10,7] 返回（3+5+7）


解题思路: 
遍历array 中的所有元素，设置两个变量： 
cur: 不包含前一个元素的最大和 
notcur: 包含前一个元素的最大和

更新当前元素的 cur 和 notcur： 
不包含当前元素的最大和 notcur = max(notcur’， cur’) 
包含当前元素的最大和 cur = notcur’+current (元素不能相邻)
'''

def sumOfOrderList(alist):

    if not alist:
        return 0

    cur = alist[0]
    notcur = 0

    for i in range(1, len(alist)):

        # if notcur > cur:
        #     notcur_new = notcur

        notcur_new = max(cur, notcur)

        cur = alist[i] + notcur

        notcur = notcur_new





    return max(notcur, cur)


print(sumOfOrderList([3,1,-5,2,4,-6]))








'''
输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。
求所有子数组的和的最大值。要求时间复杂度为O(n)。 
'''


def sumOfchildList(alist):


    cursum = 0

    maxsum = 0
    for i in range(len(alist)):
        cursum += alist[i]
        if cursum <= 0:
            cursum = 0

        if maxsum < cursum:
            maxsum = cursum


    # all number<0 in list
    if maxsum == 0:
        maxsum = alist[0]
        for i in range(1, len(alist)):
            if alist[i] > maxsum:
                maxsum = alist[i]


    return maxsum

    #all number<0


# print(sumOfchildList([1,-2,3,10,-4,7,2,-5]))
#
# print(sumOfchildList([-2,-1,-10,-5]))