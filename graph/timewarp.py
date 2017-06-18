#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:49:23 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/TIMETRIP
"""
import sys 
import math
input = sys.stdin.readline 

class Graph(object):
    def __init__(self,g):
        #최단 시간으로 이동하는경우 
        self.spent_yrs = [[math.inf for _ in range(g)] for _ in range(g)] 
        for i in range(g):
            self.spent_yrs[i][i] = 0
                          
    def set_yrs_spent(self,a,b,d):
        self.yrs_spent[a][b] = d 
    
    def set_yrs_spent_max(self):
        #최장 시간으로 이동하는 경우
        self.yrs_spent_max = self.yrs_spend[:]
        
def get_time_change(graph,g):
    #floyd_warshall algorithm     
    for k in range(g):
        for i in range(g):
            for j in range(g):
                if graph.yrs_spent[i][j] > graph.yrs_spent[i][k]+graph.yrs_spent[k][j]:
                    graph.yrs_spent[i][j] = graph.yrs_spent[i][k]+graph.yrs_spent[k][j]
                if graph.yrs_spent_max[i][j] > graph.yrs_spent_max[i][k]+graph.yrs_spent_max[k][j]:
                    graph.yrs_spent_max[i][j] = graph.yrs_spent_max[i][k]+graph.yrs_spent_max[k][j]
    
if __name__=='__main__':
    testcases = int(input())
    for case in range(testcases): 
        (g,w) = tuple(int(x) for x in input().split())
        graph = Graph(g)
        for wormhole in range(w):
            #웜홂 a->b 이동하는데 d년 만큼 시간이 변화 
            (a,b,d) = tuple(int(x) for x in input().split())
            graph.set_yrs_spent(a,b,d)
        graph.set_yrs_spent_max()
        graph.get_time_change(graph,g)
        print(graph.set_yrs_spent[0][1], graph.set_yrs_spent_max[0][1])
            
        

