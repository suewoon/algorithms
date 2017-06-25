#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:27:30 2017

@author: suewoonryu

square grid implementation
"""

class SquareGrid(object):
    def __init__(self,grid):
        self.grid = []
        self.width = len(self.grid[0]) 
        self.height = len(self.grid) 
        self.walls = []
        self.blank = self.find_blank()
        
    def in_bounds(self, id):
        '''
        if (x,y) is inside the grid 
        '''
        (x,y) = id 
        return 0<= x < self.width  and 0<= y < self.height
    
    def passable(self, id):
        '''
        if (x,y) is not on the wall 
        '''
        return id not in self.walls
    
    def find_blank(self):
        '''
        find a blank in the 15 puzzle grid 
        '''
        for i in self.grid:
            for j in self.grid[i]:
                if j == 0 : 
                    self.blank=(i,j)
                    return self.blank
        
    def neighbors(self,id=find_blank()):
        '''
        return neighbors's coordinate in the list 
        '''
        (x,y) = id 
        results = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        results = filter(self.in_bounds, results)
        #results = filter(self.passable, results)
        return results
    
    def apply_move(self,id):
        (x,y) = id
        blank_x = self.blank[0]
        blank_y = self.blank[1]
        next_grid = [row[:] for row in self.grid]
        next_grid[blank_x][blank_y]=next_grid[blank_x+y][blank_y+x]
        next_grid[blank_x+y][blank_y+x]=0
        return next_grid
        
        
        
    