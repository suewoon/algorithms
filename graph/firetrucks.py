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
        self.graph = [[ 0 for _ in range(v)] for _ in range(v)]
        self.fire_station = []
        self.fire_area=[]
        
    def add_edge(self,id1,id2,time):
        self.graph[id1][id2] = time 
        self.graph[id2][id1] = time

def min_taking_time(graph):
    time_in_total = 0
    for area in graph.fire_area:
        time = 1000000
        for station in graph.fire_station: # firestation 에서만 출발 할 수 있음
            elements = []
            heapq.heappush(elements,(0,station))
            
            time_so_far = {}
            time_so_far[station]=0
                       
            while len(elements)>0:
                current = heapq.heappop(elements)[1]
                if current == area :
                    time_so_far[area] <  time
                    time = time_so_far[area]
                
                for neighbor in graph.graph[current]:
                    new_time = time_so_far[current]+graph.graph[current][neighbor]
                    if neighbor not in time_so_far or new_time < time_so_far[neighbor]:
                        time_so_far[neighbor] = new_time 
                        heapq.heappush(elements,(new_time,neighbor))
        time_in_total += time
        
        
               
if __name__=='__main__':
    testcases = int(input())
    for i in range(testcases):
        #v : 장소의 수, e:도로의 수, n:화재 장소의 수, m:소방서의 수 
        (v,e,n,m)=tuple(int(x) for x in input().split())
        g = Graph(v)
        for j in range(e):
            (a,b,time)=tuple(int(x) for x in input().split())
            b.add_edge(a,b,time)
        g.fire_area = [int(x)for x in input().split()]
        g.fire_station = [int(x) for x in input().split()]
        print(g.graph)
        print(g.fire_station)
        print(g.fire_area)
        #print(min_taking_time(g))