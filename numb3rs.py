#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 00:09:02 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/NUMB3RS

return the probability of reaching certain nodes given the starting point s
"""

class Breakout(object):
    def __init__(self, adj, destinations):
        self.transform(adj)
        self.destinations = destinations

    def transform(self, adj):
        '''
        transform the adjacent matrix into graph 
        '''
        self.graph = {}
        for i in range(len(adj)):
            self.graph[i] = []
            for j in range(len(adj[i])):
                if adj[i][j] == 1:
                    self.graph[i].append(j)
                    
    def get_prob_helper(self,source, destination, days_after):
        if days_after==0 : 
            if source == destination:
                return 1 
            else : 
                return 0
        else : 
            prob_sum = 0.0
            for neighbor in self.graph[source] : 
                if len(self.graph[source]) !=0 :
                    prob_sum += self.get_prob_helper(neighbor, destination,days_after-1)/(len(self.graph[source]))
            return prob_sum 
    
    def get_prob(self, source, days_after):
        for destination in self.destinations : 
            print(self.get_prob_helper(source, destination, days_after), end=' ')

testcases = int(input())
for i in range(testcases):
    (N,D,P) = tuple(int(x) for x in input().split()) #N: the number of nodes, D:days after, P:starting node
    adj = [ [int(x) for x in input().split()] for i in range(N)]
    T = int(input())
    Q = [int(x) for x in input().split()]
    b = Breakout(adj,Q)
    b.get_prob(P,D)




