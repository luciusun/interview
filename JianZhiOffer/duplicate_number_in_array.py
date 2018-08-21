#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note:
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有
几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
'''

__author__ = 'slucius'



class Solution:
    def duplicate(self, numbers, duplication):
        #boundary test
        if len(numbers) == 0:
            return False

        s = set(numbers)
        # onlyList = [x for x in s]
        for x in s:
            numbers.remove(x)

        #special value TEST [1,2,3,4]
        if len(numbers) != 0:
            duplication[0] = numbers[0]
        else:
            return False

        return True


    def duplicate1(self, numbers, duplication):
        d = dict()
        for i in numbers:
            # if not d.has_key('i'):
            if i not in d:
                d[i] = 1

            else:
                d[i] += 1
                duplication.append(i)


        # return d, duplication
        if len(duplication) != 0:

            return duplication[0]
        else:
            return False



# a = Solution()
# print(a.duplicate1([2,3,1,0,2,5,3], [])

a = [2,3,1,0,2,5,3]
d = dict()
for key in a:
    d[key] = d.get(key, 0) + 1

for j in d:
    if d[j] > 1:
        print(j)

print(d)
