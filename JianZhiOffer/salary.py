#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'

import sys

def salary(money):
    s1 = 90
    s2 = 900
    s3 = 2600
    s4 = 2500
    s5 = 6000
    s6 = 8750
    if(money<=5000):
        return 0
    if(money>5000):
        temp = money - 5000
        if(temp<=3000):
            val1 = temp * 0.03
            val = int(temp * 0.03)
            if (val1 - val) >= 0.5:
                return val + 1
            return val
        elif(temp<=12000):
            val1 = s1 + (temp-3000)*0.1
            val = int(s1 + (temp-3000)*0.1)
            if (val1 - val) >= 0.5:
                return val + 1
            return val
        elif(temp<=25000):
            val1 = s1 + s2 + (temp-12000)*0.2
            val = int(s1 + s2 + (temp-12000)*0.2)
            if (val1 - val) >= 0.5:
                return val + 1
            return val
        elif(temp<=35000):
            val1 = s1 + s2 + s3 + (temp - 25000)*0.25
            val = int(s1 + s2 + s3 + (temp - 25000)*0.25)
            if (val1 - val) >= 0.5:
                return val + 1
            return val
        elif (temp <= 55000):
            val1 = s1 + s2 + s3 + s4 + (temp - 35000)*0.3
            val = int(s1 + s2 + s3 + s4 + (temp - 35000)*0.3)
            if (val1 - val) >= 0.5:
                return val + 1
            return val
        elif (temp <= 80000):
            val1 = s1 + s2 + s3 + s4 + s5 + (temp - 55000)*0.35
            val = int(s1 + s2 + s3 + s4 + s5 + (temp - 55000)*0.35)
            if (val1 - val) >= 0.5:
                return val + 1
            return val
        else:
            val1 = s1 + s2 + s3 + s4 + s5 + s6 + (temp - 80000)*0.35
            val = int(s1 + s2 + s3 + s4 + s5 + s6 + (temp - 80000)*0.35)
            if (val1 - val) >= 0.5:
                return val + 1
            return val

# print(salary(10001))
with open('bbox.txt') as f:
    n = int(f.readline().strip())
    for i in range(n):
        s = int(f.readline().strip())
        print(salary(s))



# if __name__ == "__main__":
#
#     n = int(sys.stdin.readline().strip())
#     # ans = 0
#     for i in range(n):
#
#         line = int(sys.stdin.readline().strip())
#         print(salary(line))

        # with open('bbox.txt') as f:
        #     n = int(f.readline().strip())
        #     for i in range(n):
        #         s = int(f.readline().strip())
        #         print(salary(s))
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     # ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         print(salary(int(line)))
# #
#         # # 把每一行的数字分隔后转化成int列表
#         # values = map(int, line.split())
        # for v in values:
        #     # ans += v
        #     salary(v)

    # print ans



# if __name__ == "__main__":
#
#
#
#     n = int(sys.stdin.readline().strip())
#     for i in range(n):
#         days = int(sys.stdin.readline().strip())
#         salary(days)
#
#
#     # n = int(sys.stdin.readline().strip())
#     # ans = 0
#     # for i in range(n):
#     #     # 读取每一行
#     #     line = sys.stdin.readline().strip()
#     #     # 把每一行的数字分隔后转化成int列表
#     #     values = map(int, line.split())
#     #     for v in values:
#     #         salary(v)
#     #         # print(salary(v))



            # ans += v
    # print(ans)