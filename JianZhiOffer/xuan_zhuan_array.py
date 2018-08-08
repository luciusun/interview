#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''document note:
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

__author__ = 'slucius'


def minNumberInRotateArray1(rotateArray):
    # write code here
    if len(rotateArray)==0:
        return 0
    else:
        #for i in rotateArray:
        min=rotateArray[0]
        for i in range(len(rotateArray)-1):
            #min=rotateArray[i]
            b=rotateArray[i+1]
            if min>=b:
                min=b
            i=i+1
        return min






def minNumberInRotateArray2(rotateArray):
    if len(rotateArray)==0:
        return 0

    first = 0
    last = len(rotateArray) - 1
    minVal = rotateArray[0]
    if(rotateArray[first] < rotateArray[last]):
        return rotateArray[first]
    else:
        while(first < last-1):
            mid = (first + last)//2
            if(rotateArray[first] > rotateArray[mid]):
                last = mid
            elif(rotateArray[mid] > rotateArray[last]):
                first = mid
            elif(rotateArray[mid]==rotateArray[first] and rotateArray[first] == rotateArray[last]):
                for i in range(1, len(rotateArray)):
                    if rotateArray[i]<minVal:
                        minVal = rotateArray[i]
                        last = i
        minVal = rotateArray[last]
        return minVal


print(minNumberInRotateArray2([3, 4, 5, 1, 2]))