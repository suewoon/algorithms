#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 13:00:46 2017

@author: suewoonryu
"""

import priorityqueue as pq
import weighted_grids as wgrid


def dijkstra_search(graph, start, goal): 
    '''
    dijkstar_search
    '''
    frontier = pq.PriorityQueue()
    frontier.put(start,0)
    
    came_from = {}
    cost_so_far = {} 
    came_from[start]=None 
    cost_so_far[start] = 0 
    while not frontier.empty():
        current = frontier.get()
        
        if current==goal : 
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current,next)
            if next not in cost_so_far or new_cost < cost_so_far[next]: # if new path to the location is better than the best previous path
                cost_so_far[next] = new_cost
                priority = new_cost 
                frontier.put(next,priority)
                came_from[next] = current 
    
    return came_from, cost_so_far 

def heuristic(a,b):
    '''
    manhattan distance on a square grid
    '''
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def greedy_best_search(graph, start,goal):
    '''
    greedy best first search 
    '''
    frontier = pq.PriorityQueue()
    frontier.put(start,0)
    
    came_from = {}
    came_from[start]=None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current==goal :
            break
        
        for next in graph.neighbors(current):
            if next not in came_from :
                priority = heuristic(goal,next)
                frontier.put(next,priority)
                came_from[next] = current
                         
    return came_from 

def reconstruct_path(came_from,start,goal):
    current = goal 
    path = [current]
    while current!=start :
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

