#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 17 21:07:40 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/HANOI4 
"""

import heapq
PEG = 4


def count_cost(came_from,start, goal):
    '''
    backtrack the path for counting steps from start to goal 
    '''
    current = goal
    path = [current]
    while current != start : 
        current = came_from[current]
        path.append(current)
    #path.reverse()
    return len(path)-1
    

def bfs(start, goal):
    '''
    원반을 begin 상태에서 end상태로 움직일 떄 최소 움직임 수 
    '''
    if start == goal : 
        return 0
    
    elements = []
    heapq.heappush(elements,(0,start))
        
    came_from = {}
    cost_so_far={}
    came_from[start]=None 
    cost_so_far[start]=0

    while len(elements)>0:
        current = heapq.heappop(elements)[1]
        if current == goal : 
            return came_from
        
        for neighbor in neighbors(current):
            new_cost = cost_so_far[current]+1
            if neighbor not in cost_so_far or new_cost <cost_so_far[neighbor] :
                cost_so_far[neighbor] = new_cost
                heapq.heappush(elements,(new_cost,neighbor))
                came_from[neighbor] = current

def neighbors(cur_state):
    '''
    get states of neighbors from current one 
    '''
    neighbors = []
    new_state=''
  
    for i in range(len(cur_state)):
        for j in range(1,PEG+1):
            if str(j) not in cur_state[:i] and str(cur_state[i]) not in cur_state[:i]:
                new_state = cur_state[:i]+str(j)+cur_state[i+1:]
                if new_state not in neighbors:
                    neighbors.append(new_state)
    neighbors.remove(cur_state)
    return neighbors
               
testcases = int(input())
for i in range(testcases):
    N = int(input())
    initial = [0 for i in range(N)]
    goal = [0 for i in range(N)]
    for i in range(4):
        arr = [int(x) for x in input().split()]
        for j in arr[1:] : 
            initial[j-1]=i+1
    initial = ''.join([str(i) for i in initial])
    print(initial)
    for i in range(4):
        arr = [int(x) for x in input().split()]
        for j in arr[1:] : 
            goal[j-1]=i+1
    goal = ''.join([str(i) for i in goal])
    print(goal)
    print(count_cost(bfs(initial,goal),initial,goal))

