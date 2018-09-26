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


def dfs2(graph, start, visited = None):
    '''recursive.'''
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start]-visited:
        dfs2(graph, next, visited)
    return visited

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

print(bfs(graph, 'A'))
