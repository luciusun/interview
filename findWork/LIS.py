#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 最长递增子序列
'''

__author__ = 'slucius'


'''
1.复杂度为O(N^2)的方法，算法很简单。dp[i]表示在以arr[i]这个数结尾的情况下，arr[0....i]中的最大递增子序列
'''


def getdpi(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


def generateLIS(arr, dp):
    n = max(dp)
    index = dp.index(n)
    lis = [0] * n
    n -= 1
    lis[n] = arr[index]
    #从右向左
    for i in range(index, 0-1, -1):
        if arr[i] < arr[index] and dp[i] == dp[index] - 1:
            n -= 1
            lis[n] = arr[i]
            index = i
    return lis






'''
2.动态规划法（O(NlogN)）,申请一个长度为N的空间，B[N]，用变量len记录现在的最长递增子序列的长度。
'''

def getdp2(arr):
    n = len(arr)
    dp = [0] * n
    ends = [0] * n
    ends[0] = arr[0]
    dp[0] = 1
    right, l, r, mid = 0, 0, 0, 0
    for i in range(1, n):
        l = 0
        r = right
        # 二分查找,若找不到则ends[l或r]是比arr[i]大而又最接近其的数
        # 若arr[i]比ends有效区的值都大，则l=right+1
        while l <= r:
            mid = (l+r)//2
            if arr[i] > ends[mid]:
                l = mid + 1
            else:
                r = mid -1
        right = max(right, l)
        ends[l] = arr[i]
        dp[i] = l + 1

    return dp



arr = [3, 5, 4, 9, 8]
dp = getdp2(arr)
print(generateLIS(arr, dp))





