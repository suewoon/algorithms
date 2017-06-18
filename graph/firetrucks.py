#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 28 13:12:26 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/FIRETRUCKS
"""
import heapq

class Graph(object):
    def __init__(self,v):
        self.graph = [[ 101 for _ in range(v+1)] for _ in range(v+1)]
        self.fire_station =[]
        self.fire_area=[]
        self.set_dummy_node(v)
        
    def add_edge(self,id1,id2,time):
        self.graph[id1-1][id2-1] = time 
        self.graph[id2-1][id1-1] = time
    
    def set_dummy_node(self,v):
        for i in self.fire_station:
            self.graph[v][i] = 0
            self.graph[i][v] = 0 
                      
    def get_neighbors(self, current):
        return [i for i in self.graph[current] if self.graph[current][i] != 101]

def min_taking_time(graph,v):
    time_in_total = 0
    
    for area in graph.fire_area:
        elements = []
        heapq.heappush(elements,(0,v))
        
        time_so_far = {}
        time_so_far[v]=0
                   
        while len(elements)>0:
            current = heapq.heappop(elements)[1]
            
            if current==area :
                time_in_total+=time_so_far[area]
                break
            
            for neighbor in graph.get_neighbors(current):
                new_time = time_so_far[current]+graph.graph[current][neighbor]
                if neighbor not in time_so_far or new_time < time_so_far[neighbor]:
                    time_so_far[neighbor] = new_time 
                    heapq.heappush(elements,(new_time,neighbor))
                    
    return time_in_total 
        
        
               
if __name__=='__main__':
    testcases = int(input())
    for i in range(testcases):
        #v : 장소의 수, e:도로의 수, n:화재 장소의 수, m:소방서의 수 
        (v,e,n,m)=tuple(int(x) for x in input().split())
        g = Graph(v)
        for j in range(e):
            (a,b,time)=tuple(int(x) for x in input().split())
            g.add_edge(a,b,time)
        g.fire_area = [int(x)for x in input().split()]
        g.fire_station = [int(x) for x in input().split()]
#        
#        print(g.graph)
#        print(g.fire_area)
#        print(g.fire_station)
        print(min_taking_time(g,v))