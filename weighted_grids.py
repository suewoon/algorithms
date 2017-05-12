#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:29:19 2017

@author: suewoonryu

weighted grids 
"""

class SquareGrid:
    def __init__(self, width, height):
        self.width = width 
        self.height=height 
        self.walls = []
    
    def in_bounds(self,id):
        (x,y) = id 
        return 0<=x<self.width and 0<=y<self.height
    
    def passable(self,id):
        return id not in self.walls 
    
    def neighbors(self, id):
        (x,y)=id 
        results = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        
        return results

class GridWithWeights(SquareGrid):
    def __init__(self, width, height):
        super().__init__(width,height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        #when there is no key in dictionary return 1. By default, same cost per step 
        return self.weights.get(to_node,1) 
