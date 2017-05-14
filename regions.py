#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:26:49 2017

@author: suewoonryu

5 7 3
0 2 4 4
1 1 2 5
4 0 6 2

https://www.acmicpc.net/problem/2583

"""
import sys
sys.setrecursionlimit(10000)

class SquareGrid(object):
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.visited=set()   
        
    def in_bounds(self, id):
        '''
        if (x,y) is inside the grid 
        '''
        (x,y) = id 
        return 0<= x < self.height  and 0<= y < self.width
    
    def passable(self, id):
        '''
        if (x,y) is not on the wall 
        '''
        return id not in self.walls
    
    def neighbors(self,id):
        '''
        return neighbors's coordinate in the list 
        '''
        (x,y) = id 
        results = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        
        return results
    
    def set_wall(self, a,b):
        (x1,y1) = a
        (x2,y2) = b 
        (x3,y3)= (self.height-y1-1,x1)
        w = abs(x1-x2)
        h = abs(y1-y2)
        
        walls = [] 
        
        for i in range(w):
            walls.append((x3,y3+i)) 
        cp=walls[:]
        for j in range(1,h):
            walls+=[(i[0]-j,i[1]) for i in cp]
        self.walls+=walls
        
        self.walls =list(set(self.walls)) #remove duplicate

#recursive dfs
def dfs(graph, coord):
    (x,y) = coord
    graph.visited.add(coord)
    for neighbor in graph.neighbors(coord):
        if neighbor not in graph.visited :
            graph.visited.add(neighbor)
            dfs(graph,neighbor)
    return 

def get_number_of_rooms(graph):
    count=0
    areas=[0]
    for i in range(graph.height):
        for j in range(graph.width):
            if (i,j) not in graph.visited and (i,j) not in graph.walls: 
                dfs(graph,(i,j))
                count+=1 
                areas.append(len(graph.visited))
    return count, areas

if __name__ == '__main__':
    (height, width, k) = tuple(int(x) for x in input().split())
    grid = SquareGrid(width,height)
    for i in range(k):
        cord = [int(x) for x in input().split()]
        grid.set_wall(cord[:2],cord[2:])
    count , areas = get_number_of_rooms(grid)
    areas = sorted([ areas[i+1]-areas[i] for i in range(len(areas)-1)])
    print(count)
    print(*areas,sep=' ')
        

