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

# utility functions for dealing with square grids
def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = "\u2192"
        if x2 == x1 - 1: r = "\u2190"
        if y2 == y1 + 1: r = "\u2193"
        if y2 == y1 - 1: r = "\u2191"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r

def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()


diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]}
