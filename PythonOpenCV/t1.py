#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'


#         self.right = None
class Solution:

    def dfs(self, root, res, path):
        if not root.left and not root.right and sum(path) == self.target:
            res.append(path)
        if root.left:
            dfs(root.left, res, path + [root.left.val])
        if root.right:
            dfs(root.right, res, path + [root.left.right])

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        self.target = expectNumber
        self.dfs(root, res, [root.val])
        return res