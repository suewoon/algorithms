e#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:52:00 2017

@author: suewoonryu
"""

import basicgraph as bg
import queue 


def dfs(graph, id1):
    '''
    depth first search given it starts searching with 'start_node'
    '''
    to_visit = []
    visited = set()
    
    to_visit.append(graph.all_vertices[id1])
    visited.add(graph.all_vertices[id1])
    
    while to_visit :
        vertex = to_visit.pop()
        print(vertex)
#       when the destination is designated        
#       if vertex == graph.all_vertices[id2]:
#            return
        for neighbor in vertex.adj_vertices : 
            if neighbor not in visited : 
                visited.add(neighbor)
                to_visit.append(neighbor) 

def bfs(graph,id1):
    '''
    breadth first search given it starts searching with 'start_node'
    '''
    to_visit = queue.Queue()
    visited = set()
    
    to_visit.put(graph.all_vertices[id1])
    visited.add(graph.all_vertices[id1])
    
    while not to_visit.empty() : 
        vertex = to_visit.get()
        print(vertex)
#        when the destination is designated 
#        if vertex == graph.all_vertices[id2]:
#            return
        
        for neighbor in vertex.adj_vertices:
            if neighbor not in visited : 
                visited.add(neighbor)
                to_visit.put(neighbor)

    

if __name__=='__main__':
#    g = bg.Graph(True)
#    g.add_edge(1,2)
#    g.add_edge(1,4)
#    g.add_edge(2,5)
#    g.add_edge(3,2)
#    g.add_edge(4,7)
#    g.add_edge(5,6)
#    g.add_edge(5,7)
#    g.add_edge(6,3)
#    g.add_edge(7,8)
#    g.add_edge(8,7)
#    g.add_edge(8,5)
#    g.add_edge(9,6)
#    g.add_edge(9,8)
#    print('bfs:')
#    bfs(g,1)
#    print('dfs:')
#    dfs(g,1)

    g2 = bg.Graph(False)
    g2.add_edge(1,4)
    g2.add_edge(2,3)
    g2.add_edge(2,5)
    g2.add_edge(2,6)
    g2.add_edge(4,5)
    print('bfs:')
    bfs(g2,1)
    print('dfs:')
    dfs(g2,1)
    
    
    