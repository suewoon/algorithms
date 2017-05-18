#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun May  7 19:21:16 2017
@author: suewoonryu
"""
import queue 

class Vertex(object):
    def __init__(self):
        self.arr = [] 
        self.edges = []
        self.adj_vertices = []
    
    def add_adj_vertices(self, edge, vertex): 
        self.edges.append(edge)
        self.adj_vertices.append(vertex)

    def __hash__(self):
        return "".join(self.arr)
    
    def __eq__(self,other):
        return ''.join(self.arr) == ''.join(other.arr)
    
    def __str__(self):
        return self.arr 
    
    def __repr__(self):
        return self.__str__()
    

class Edge(object): 
    def __init__(self, v1, v2):
        self.v1 = v1 
        self.v2 = v2 
        
    def __hash__(self):
        return hash(self.v1)+hash(self.v2 )
    
    def __eq__(self,other):
        return self.v1.id==other.v1.id and self.v2.id==other.v2.id

    
    
class Graph(object): 
    def __init__(self):
        self.all_edges = []
        self.all_vertices = {}

    def add_edge(self,id1,id2):
        return
    
    def bfs(self, start_arr):
        end = ''.join(sorted(start_arr))
        start=''.join(start_arr)
        length = len(start_arr)
        
        visited = set()
        to_visit = queue.Queue()
        
        to_visit.put(self.all_vertices[start])
        visited.add(self.all_vertices[start])
        distance = {}
        
        while not to_visit.empty():
            vertex = to_visit.get()
#            print(vertex)
            
            if vertex == self.all_vertices(end):
                return distance[vertex]
            
            
            for neighbor in vertex.adj_vertices : 
                if neighbor not in visited : 
                    visited.add(neighbor)
                    to_visit(neighbor)


def reverse(sofar, rest):
    if len(sofa)
        


'''
solution for https://algospot.com/judge/problem/read/SORTGAME
'''

if __name__=='__main__':
    testcases = int(input())
    for i in range(testcases):
        length = int(input())
        seq = [ int(x) for x in input().split()]
        
        
        
        