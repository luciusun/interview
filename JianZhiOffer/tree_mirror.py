#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 二叉树的镜像: 操作给定的二叉树，将其变换为源二叉树的镜像。
'''

__author__ = 'slucius'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    # 递归实现
    def Mirror(self, root):
        if not root:
            return None
        if root.left == None and root.right == None:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.Mirror(self.left)
        self.Mirror(self.right)


    #stack 非递归实现
    def Mirror1(self, root):
        if not root:
            return None
        stackNode = []
        stackNode.append(root)
        while len(stackNode) > 0:
            nodeNum = len(stackNode) - 1
            tree = stackNode[nodeNum]
            stackNode.pop()
            nodeNum -= 1
            if tree.left != None or tree.right != None:
                tree.left, tree.right = tree.right, tree.left
            if tree.left:
                stackNode.append(tree.left)
            if tree.right:
                stackNode.append(tree.right)


    # queue 非递归实现
    def Mirror2(self, root):
        if not root:
            return None
        nodeQue = [root]
        while len(nodeQue) > 0:
            curLevel, count = len(nodeQue), 0
            while count < curLevel:
                count += 1
                pRoot = nodeQue.pop(0)
                pRoot.left, pRoot.right = pRoot.right, pRoot.left
                if pRoot.left:
                    nodeQue.append(pRoot.left)
                if pRoot.right:
                    nodeQue.append(pRoot.right)









