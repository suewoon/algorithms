#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 21:17:51 2017

@author: suewoonryu

solution for : https://algospot.com/judge/problem/read/GALLERY
"""

class SensorPlacement(object):
    def __init__(self):
        return 
    
    def insert_node(self, nodes):
        return 
    
    def get_max_sensors(self):
        return
    
testcases = int(input())
for i in range(testcases):
    s = SensorPlacement()
    (g,h) = tuple(int(x) for x in input().split())  
    for j in range(h):
        s.insert_node([int(x) for x in input().split()])
    print(s.get_max_sensors())