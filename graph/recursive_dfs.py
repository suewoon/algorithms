#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 07:45:59 2017

@author: suewoonryu

recursive depth-first search
"""
              
def dfs(graph, start, visited=None):
    if visited is None : 
        visited = []
    visited.append(start)
    for next in set(graph[start]) - set(visited) : 
        dfs(graph, next, visited)
    return visited 

graph = {
        'A' : ['B','G'],
        'B' : ['A','F'],
        'C' : ['E','D','H'],
        'D' : ['C','E'],
        'E' : ['H'],
        'F' : ['B'],
        'G' : ['A'],
        'H' : ['E','C']
        }
