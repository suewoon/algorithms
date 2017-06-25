#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 11:58:06 2017

@author: suewoonryu
"""

import sys
input = sys.stdin.readline

class Graph(object):
    def __init__(self):
        #최단 시간으로 이동하는경우
        self.yrs_spent={}
    def set_yrs_spent(self,line):
        (a,b,d) = tuple(int(x) for x in line.split())
        if a not in self.yrs_spent:
            self.yrs_spent[a]=[(b,d)]
        else :
            self.yrs_spent[a].append((b,d))

def initialize(graph,source,g):
    d = {} #destination
    for node in range(g):
        d[node] = float('inf')
    d[source] = 0
    return d

def relax(node, neighbor_list, d,is_max):
    neighbor = neighbor_list[0] 
    cost = neighbor_list[1]
    if is_max:
        cost  =  cost*-1 
    if d[neighbor] > d[node]+cost :
        d[neighbor] = d[node]+cost

def get_time_change(graph,source,g,is_max=False):
    try:
        d = initialize(graph,source,g)

    #bellman-ford algorithm
        for i in range(g-1):
            for u in graph:
                for v in graph[u]:
                    relax(u,v,d,is_max)

    # negative-weight cycle check
        for node  in graph:
            for neighbor_list in graph[u]:
                neighbor = neighbor_list[0]
                cost = neighbor_list[1]
                assert d[neighbor] <= d[u]+cost
    
    except AssertionError: 
        d[neighbor]=1001 

    return d

if __name__=='__main__':
    testcases = int(input())
    for case in range(testcases): 
        (g,w) = tuple(int(x) for x in input().split())
        graph = Graph()
        for wormhole in range(w):
            #wormhole a->b 이동하는데 d년 만큼 시간이 변화 
            graph.set_yrs_spent(input())
        min_d  = get_time_change(graph.yrs_spent,0,g)
        min_time = min_d[1] if min_d[1]!= float('inf') else 'UNREACHABLE'
        if min_time == 'UNREACHABLE':
            print(min_time)
        else : 
            max_d = get_time_change(graph.yrs_spent,0,g,True) 
            max_time = -max_d[1] 
            print(min_time, max_time) 
