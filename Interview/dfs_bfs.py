#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = 'slucius'


graph = {
    'A':set(['B', 'C']),
    'B':set(['A', 'D', 'E']),
    'C':set(['A', 'F']),
    'D':set(['B']),
    'E':set(['B', 'F']),
    'F':set(['E', 'C'])

}

# print(graph)

def dfs(graph, start):

    stack = []
    visted = set()
    stack.append(start)
    while stack:
        vertex = stack.pop()
        # visted.add(vertex)
        if vertex not in visted:
            visted.add(vertex)
            stack.extend(graph[vertex] - visted)
    return visted


# print(dfs(graph, 'A'))


def bfs(graph, start):

    queue = []
    visited = set()
    queue.append(start)

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[start]-visited)

    return visited



nodes = [i for i in range(1, 9)]
sides = [(1,2),(1, 3),(2, 4),(2, 5),(4, 8),(5, 8),(3, 6),(3, 7),(6, 7)]



class Graph(object):


    def __init__(self, nodes, sides):
        self.tmp = []
        self.sequence = {}

        for node in nodes:
            for side in sides:
                if node == side[0]:
                    self.tmp.append(side[1])
                elif node == side[1]:
                    self.tmp.append(side[0])
            self.sequence[node] = self.tmp
            self.tmp = []



    def dfs(self, node0):

        stack = []
        order = []
        stack.append(node0)

        while stack:
            vertex = stack.pop()
            order.append(vertex)

            for i in self.sequence[vertex]:
                if i not in order and i not in stack:
                    stack.append(i)
        return order


    def bfs(self, node0):

        queue = []
        order = []
        queue.append(node0)
        order.append(node0)

        while queue:
            vertex = queue.pop(0)
            # order.append(vertex)

            for i in self.sequence[vertex]:
                if i not in order:
                    queue.append(i)
                    order.append(i)
        return order



# g = Graph(nodes, sides)
# print(g.dfs(2))

