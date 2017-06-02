#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:52:28 2017

@author: suewoonryu

https://algospot.com/judge/problem/read/ROUTING
"""

import heapq

# --> adj matrix로 풀어볼것 
class Graph(object):
    def __init__(self):
        self.edges = {}
        self.graph_matrix = {}
    
    def add_edge(self,id1,id2,weight):
        if id1 in self.graph_matrix : 
            self.graph_matrix[id1].append(id2)
        else : 
            self.graph_matrix[id1] = [id2]
         
        if id2 in self.graph_matrix :
            self.graph_matrix[id2].append(id1)
        else : 
            self.graph_matrix[id2] = [id1]
              
        self.edges[str(id1)+str(id2)] = weight
        self.edges[str(id2)+str(id1)] = weight 

def dijkstar(graph,start,goal):
    elements = []
    heapq.heappush(elements,(0,start)) 
    
    cost_so_far = {}
    cost_so_far[start]=1
    
    if start == goal : 
        return cost_so_far[start]
    
    while len(elements)>0 : 
        current = heapq.heappop(elements)[1]
        if current == goal : 
            return cost_so_far[goal]
        
        for neighbor in graph.graph_matrix[current] : 
            weight_of_edge = graph.edges[str(current)+str(neighbor)]
            new_cost = cost_so_far[current]*weight_of_edge
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost 
                priority = new_cost 
                heapq.heappush(elements,(priority, neighbor))
                       
if __name__=='__main__':
    testcases = int(input())
    for i in range(testcases):
        (N,M) = tuple(int(x) for x in input().split())
        graph = Graph()
        for j in range(M):
            (node1, node2, weight) = tuple(input().split())
            graph.add_edge(node1,node2,float(weight))
        print(dijkstar(graph,'0',str(N-1)))