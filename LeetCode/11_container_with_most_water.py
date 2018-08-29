#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 盛最多水的容器.
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水.
'''

__author__ = 'slucius'

#方法一：暴力法

#方法二：双指针法,两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。

def findMaxArea(alist):
    if not alist or len(alist) < 2:
        return None


    ileft = 0
    iright = len(alist)-1
    maxArea = (iright-ileft)*(min(alist[ileft], alist[iright]))

    while ileft < iright:
        if alist[ileft] < alist[iright]:
            ileft += 1
        else:
            iright -= 1

        curArea = (iright-ileft)*(min(alist[ileft], alist[iright]))
        if curArea > maxArea:
            maxArea = curArea
    return maxArea

print(findMaxArea([1,8,6,2,5,4,8,3,7]))

