#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'slucius'


#print binary tree depth



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def depthTree(self, root):
        if root == None:
            return 0

        l = self.depthTree(root.left)
        r = self.depthTree(root.right)

        return max(l, r) + 1



# def depthOfTree(root):
#     if root == None:
#         return 0
#
#     ldepth = depthOfTree(root.left)
#     rdepth = depthOfTree(root.right)
#
#     return max(ldepth, rdepth) + 1




pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(8)
pRoot9 = TreeNode(9)
pRoot10 = TreeNode(2)
pRoot11 = TreeNode(9)
pRoot12 = TreeNode(2)

pRoot8.left = pRoot9
pRoot8.right = pRoot10

pRoot9.left = pRoot11
pRoot9.right = pRoot12

pRoot3.right = pRoot8

s = Solution()
print(s.depthTree(pRoot1))

# print(depthOfTree(pRoot1))



