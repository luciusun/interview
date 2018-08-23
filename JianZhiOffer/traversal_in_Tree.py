#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 树的几种遍历算法
'''

__author__ = 'slucius'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.treenode = []


    '''(1)BST中序遍历'''

    def midTravelsal_in_BST1(self, pRoot):
        if len(self.treenode) < 0:
            return None

        if pRoot.left:
            self.midTravelsal_in_BST1(pRoot.left)
        self.treenode.append(pRoot)
        if pRoot.right:
            self.midTravelsal_in_BST1(pRoot.right)



    '''(2)BST中序遍历'''

    def midTravelsal_in_BST2(self, pRoot):
        if not pRoot:
            return None

        treeStack = []
        nodesQue = []
        pNode = pRoot
        while pNode or len(treeStack):
            while pNode:
                treeStack.append(pNode)
                pNode = pNode.left

            if len(treeStack):
                pNode = treeStack.pop()
                nodesQue.append(pNode)
                pNode = pNode.right
        return  nodesQue



    '''(3)层序遍历, 中间需要队列做转存'''

    def levelTraversal(self, root):
        if not root:
            return None
        queue = []


        result = []
        queue.append(root)
        while len(queue) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)

            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)

        return result






'''
https://www.cnblogs.com/bjwu/p/9284534.html
二叉树(前序，中序，后序，层序)遍历递归与循环的python实现
'''

class Solution1:
    #中序遍历 + 递归实现
    def midTraversal_recursion(self, root):
        if not root:
            return []
        return self.midTraversal_recursion(root.left) + [root.val] + self.midTraversal_recursion(root.right)

    #中序遍历 + 循环实现
    #对于树的遍历，循环操作基本上要用到栈(stack)这个结构
    def midTraversal_loop(self, root):
        if not root:
            return []

        stack = []
        curr = root
        result = []
        # stack.append(root)
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
        return result




    # 前序遍历 + 递归实现
    def preorderTraversal_recursion(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal_recursion(root.left) + self.preorderTraversal_recursion(root.right)

    # 前序遍历 + 循环实现
    def preorderTraversal_loop(self, root):
        if not root:
            return []
        stack = []
        result = []
        curr = root
        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return result





    # 后序遍历 + 递归实现
    def postorderTraversal_recursion(self, root):
        if not root:
            return []
        return self.postorderTraversal_recursion(root.left) + self.postorderTraversal_recursion(root.right) + [root.val]


    # 后序遍历 + 循环实现
    #前序遍历：中左右，则中右左只需要在前序遍历的代码上小部分改动。倒过来则满足后序遍历; 后序遍历：左右中

    def postorderTraversal_loop(self, root):
        if not root:
            return []

        curr = root
        stack = []
        result = []
        while stack or curr:
            if curr:
                result.append(root.val)
                stack.append(root.left)
                curr = curr.right
            else:
                curr = stack.pop()

        return result[::-1]




    #层序遍历 +  递归实现
    def levelOrder_recursion(self, root):

        #result每一个子列表保存了对应index层的从左到右的所有结点value值.
        result = [[]]

        def helper(node, level):
            if not node:
                return
            else:
                result[level-1].append(node.val)
                if len(result) == level:
                    result.append([])
                helper(node.left, level+1)
                helper(node.right, level + 1)
        helper(root, 1)
        return result[:-1]















