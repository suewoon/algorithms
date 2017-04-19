#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 23:51:33 2017

@author: suewoonryu

graph nodes iteration - BFS, DFS
"""
import string 
import queue 

class Path(object):
    def __init__(self, node=None, path_length=0):
        self.node = node ,
        self.path_length = path_length
        
        
class Graph(object):
    def __init__(self):
        self.graph = {}
        self.make_test_graph()
        
    def make_test_graph(self):
        all_nodes = []
        for char in string.ascii_uppercase:
            node = char
            all_nodes += node 
            self.graph[node] = []
        for i in range(len(all_nodes)):
            for j in range(i+1, i+3):
                if j<len(all_nodes):
                    node1 = all_nodes[i]
                    node2 = all_nodes[j]
                    self.graph[node1] += node2 
                    self.graph[node2] += node1
          
        
    def dfs(self,start_node):
        '''
        depth first search given it starts searching with 'start_node'
        '''
        visited_nodes = set()
        to_visit = []
        to_visit.append(start_node)
        while to_visit : 
            next_node = to_visit.pop()
            if not visited_nodes.__contains__(next_node) : 
                print('Visiting : ' + next_node)
                visited_nodes.add(next_node)
                for neighbor in self.graph[next_node]:
                    to_visit.append(neighbor)
#            else :
#                print('Already Visiting : '+ next_node)


    def bfs(self,start_node):
        '''
        breadth first search given it starts searching with 'start_node'
        '''
        visited_nodes = set()
        to_visit = queue.Queue(0)
        p = Path(start_node,0)
        while not to_visit.empty():
            next_path = to_visit.get()
            if not visited_nodes.__contains__(next_node):
                print("Reached: ",next_path.node,"Path length: ",next_path.path_length)
                visited_nodes.add(next_path.node)
                for neighbor in self.graph[next_node.node]:
                    newPath
        
if __name__ == "__main__":   
    g = Graph()
    start_node = 'A'
    g.dfs(start_node)
          g.bfs(start_node)
    
