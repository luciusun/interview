#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 将k个排好序的链表合并成一个
'''

__author__ = 'slucius'


class Solution(object):

    #方法一：线性合并（TLE）
    def mergeOne(self, lists):
        '''
        :param lists: list[nodes]
        :return: list
        '''
        k = len(lists)
        if k == 0:
            return None
        left = lists[0]
        for i in range(1, k):
            left = self.merge(left, lists[i])
        return left

    #方法二：归并合并（AC）
    def mergeTwo(self, lists):
        if not lists:
            return None
        k = len(lists)
        return self.helper(lists, 0, k-1)

    def helper(self, lists, l, r):
        if l < r:
            m = (r + l) // 2
            left = self.helper(lists, l, m)
            right = self.helper(lists, m+1, r)
            return self.merge(left, right)
        else:
            return lists[l]



    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


    #方法三：基于堆排序的归并（AC）
    def mergeKLists(self, lists):




s = Solution()
print(s.mergeTwo([[2,4,5,8], [1,2,3,7,10], [2,4,6,8]]))