#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 11:39:15 2017

@author: suewoonryu

priority queue implementation 
"""

import heapq 

class PriorityQueue(object):
    def __init__(self):
        self.elements = [] 
    
    def empty(self):
        return len(self.elements) == 0 
    
    def put(self, item, priority): 
        '''add item with priority'''
        heapq.heappush(self.elements, (priority, item))
        
    def get(self): 
        '''return item with lowest priority'''
        return heapq.heappop(self.elements)[1]