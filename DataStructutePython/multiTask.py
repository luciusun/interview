#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 廖雪峰: 多进程
'''

__author__ = 'slucius'


# import os
#
# print('Process (%s) start...' %os.getpid())
# pid = os.fork()
# if pid == 0:
#     # print('I am child process (%s) and my parent is %s.' %(os.getpid(), os.getpgid()))
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
#     # print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' %(os.getpid(), pid))



#多线程: threading高级模块

import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n+1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
