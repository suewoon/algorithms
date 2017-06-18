#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:32:47 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/DRUNKEN
"""

import sys
import math 
input = sys.stdin.readline 

class Graph(object):
    def __init__(self,v): 
        self.dist_table= [[math.inf for _ in range(v)] for _ in range(v)] #table of shortest-path between all pairs of vertices
        self.set_diagonal(v)
        
    def set_dist(self, id1, id2, cost):
        #undirected 
        self.dist_table[id1-1][id2-1] = cost 
        self.dist_table[id2-1][id1-1] = cost 
    
    def set_diagonal(self,v):
        for i in range(v):
            self.dist_table[i][i]=0  
    
    def set_time_delay(self, time_delay):
        self.time_delay = time_delay
    
def floyd_warshall(graph,v):
    default_delay=graph.time_delay[0]
    total_time = graph.dist_table[:]
    for k in range(1,v):
        delay=graph.time_delay[k]
        for i in range(v):
            for j in range(v):
                if graph.dist_table[i][j] > graph.dist_table[i][k] + graph.dist_table[k][j]:
                    graph.dist_table[i][j]= graph.dist_table[i][k] + graph.dist_table[k][j]
                total_time[i][j] = min(total_time[i][k]+delay+total_time[k][j],total_time[i][j]+default_delay)
    return total_time

if __name__ == '__main__' : 
    (v,e) = tuple(int(x) for x in input().split())
    time_delay = [int(x) for x in input().split()]
    
    graph = Graph(v)
    graph.set_time_delay(time_delay)
     
    for edge in range(e):
        (id1, id2, cost)=tuple(int(x) for x in input().split())
        graph.set_dist(id1,id2,cost)
    
    testcases = int(input())
    
    for case in range(testcases):
        (start,end) = tuple(int(x) for x in input().split())
        time_taken = floyd_warshall(graph,v)
        print(time_taken[start][end])