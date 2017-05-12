#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:17:51 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/GALLERY
"""

class SensorPlacement(object):
    def __init__(self,nodes,edges):
        self.nodes = nodes
        self.edges = edges
        self.graph = {}
        self.initialize_graph()
        self.sensors = 0
        self.visited = set()
        
    def initialize_graph(self):
        '''
        initialize a graph with keys 
        '''
        keydict = {i for i in range(nodes)}
        self.graph = dict([ (key,[]) for key in keydict ])
        
    def insert_node(self, nodes):
        '''
        연결된 두 노드가 주어질때 그래프에 노드 삽입
        '''
        self.graph[nodes[0]].append(nodes[1])
        self.graph[nodes[1]].append(nodes[0])
    
    def return_node(self):
        '''
        return a non-visitednode with max edges 
        '''
        node_with_max_edges = -1
        max_edge = 0 
        for i in set(self.graph.keys()).difference(self.visited):
           if len(self.graph[i]) > max_edge:
               max_edge = len(self.graph[i])
               node_with_max_edges = i 
        return node_with_max_edges
    
    def bfs(self,start_node):
        '''
        iterate over graph for one depth 
        '''
        if start_node not in self.visited : 
            self.visited.add(start_node)
            self.sensors += 1
            for neighbor in self.graph[start_node]:
                self.visited.add(neighbor)
        
    def get_max_sensors(self):
        while len(self.visited)<=self.nodes:
            start_node = self.return_node()
            self.bfs(start_node)
        return self.sensors
    
testcases = int(input())
for i in range(testcases):
    (nodes,edges) = tuple(int(x) for x in input().split())  
    s = SensorPlacement(nodes,edges)
    for j in range(edges):
        s.insert_node([int(x) for x in input().split()])
    #print(s.get_max_sensors())