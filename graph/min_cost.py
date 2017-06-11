#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 19:59:15 2017

@author: suewoonryu

https://www.acmicpc.net/problem/1916
"""

import heapq as pq 

class Graph(object):
    def __init__(self, n):
        self.graph = [ [0 for _ in range(n)] for _ in range(n)]
    
    def make_graph(self,start,end,cost):
        if self.graph[start-1][end-1]==0 or cost < self.graph[start-1][end-1] :
            self.graph[start-1][end-1] = cost 
    
    def neighbors(self, current):
        neighbors = [ idx+1 for idx in range(len(self.graph)) if self.graph[current-1][idx] !=0]
        #print(current, neighbors)
        return neighbors
    
    def find_min_path(self,start,end):
        frontier = []
        pq.heappush(frontier, (0,start))
        
        came_from = {}
        cost_so_far = {}
        
        came_from[start]=None 
        cost_so_far[start]=0
        
        while not len(frontier)==0 :
            current = pq.heappop(frontier)[1]
            
            if current == end : 
                break
            
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current]+self.graph[current-1][next-1]

                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next]= new_cost
                    pq.heappush(frontier,(new_cost,next))
                    came_from[next] = current 
                    #print("came from",came_from)
                    #print("cost",cost_so_far)
        return came_from
    
    def count_cost(self,came_from,start,goal):
        current=goal 
        total_cost = 0
        path = [current]
        
        while current!=start : 
            total_cost += self.graph[came_from[current]-1][current-1]
            current = came_from[current]
            path.append(current)
        
        #print(path)
        return total_cost
        
        
    
if __name__== '__main__':
    num_of_city = int(input())
    num_of_buses = int(input())
    graph = Graph(num_of_city)
    for i in range(num_of_buses):
        #itineraire information 
        (start,end,cost) = tuple( int(x) for x in input().split())
        graph.make_graph(start,end,cost)
    #get the min cost to travel from start point to end point 
    (start,end) = tuple(int(x) for x in input().split())
    total_cost = graph.count_cost(graph.find_min_path(start,end),start,end)
    print(total_cost)