#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: DFS and BFS
'''

__author__ = 'slucius'


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
    }

# print(graph)


def dfs1(graph, start):
    '''
    1.stack
    2.Mark the current vertex as being visited.
    3.Explore each adjacent vertex that is not included in the visited set.
    '''

    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

# print(dfs(graph, 'A'))


# def dfs2(graph, start, visited = None):
#     '''recursive.'''
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start]-visited:
#         dfs2(graph, next, visited)
#     return visited

# print(dfs2(graph, 'C'))


def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex]-set(path):
            if next == goal:
                yield path+[next]
            else:
                stack.append((next, path+[next]))

# print(list(dfs_path(graph, 'A', 'F')))



def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)
    return visited

# print(bfs(graph, 'A'))




####################################################################################################


class Graph(object):
    def __init__(self, nodes, sides):
        self.sequence = {}
        self.tmp = []

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
            v = stack.pop()
            order.append(v)

            for w in self.sequence[v]:
                if w not in stack and w not in order:
                    stack.append(w)
        return order


    # def dfs_recursive(self, node0, visited = None):
    #     if visited == None:
    #         visited = []
    #
    #     visited.append(node0)
    #     for w in self.sequence[]

    def dfs2(self, node0, visited=None):
        '''recursive.'''
        if visited is None:
            visited = []
        visited.append(node0)
        for w in self.sequence[node0]:
            if w not in visited:
                self.dfs2(w, visited)
        return visited




    def bfs(self, node0):
        queue = []
        order = []
        queue.append(node0)
        order.append(node0)

        while queue:
            v =queue.pop(0)

            for w in self.sequence[v]:
                if w not in order:
                    queue.append(w)
                    order.append(w)
        return order








nodes = [i+1 for i in range(8)]

sides = [(1, 2),(1, 3),(2, 4),(2, 5),(4, 8),(5, 8),(3, 6),(3, 7),(6, 7)]

G = Graph(nodes, sides)

print(G.dfs(2))
print(G.dfs2(2))
# print(G.sequence)