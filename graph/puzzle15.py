#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 23:56:26 2017

@author: suewoonryu

puzzle 15 ; simple sliding tiles on a 4*4 grid. allowed to move along with 
empty block one step at a time. 
"""
import priorityqueue as pq
import squaregrid as sgrid
     
class SolverState(object):
    '''
    stores the current position of all numbers in the grid 
    & list of steps to get there from the beginning 
    '''
    def __init__(self,grid,steps=[]):
        self.grid = grid # 4*4 grid
        self.steps = steps
    
    def __hash__(self):
        seq=''
        for i in self.grid.grid : 
            for j in i : 
                seq+=str(j)
        return seq
    
    def solved(self):
        '''
        The puzzle is solved state, when it has sequential arrangement of the numbers 
        '''
        return self.__hash__() == '123456789101112131415'


def heuristic(a,b):
    '''
    h = sum of steps 
    '''
    (x1,y1) = a
    (x2,y2) = b
    
    return abs(x1-x2)+abs(y1-y2)

def solve(start_grid):
    frontier = pq.PriorityQueue() 
    start_state = SolverState(start_grid,[])
    frontier.put(start_state,0)
    
    came_from = {}
    cost_so_far = {}
    came_from[start_state] = None 
    cost_so_far[start_state] = 0
    
    while not frontier.empty() : 
        cur_state = frontier.get()
        
        if cur_state.solved:
            return cur_state.steps 
        
        candidate_moves = cur_state.grid.neighbors()
        
        for move in candidate_moves:
            next_grid = cur_state.grid.apply_move(move)
            next_steps = cur_state.steps.concat([move])
            next_state = SolverState(next_grid, next_steps)
            priority=1+heuristic()
            frontier.put(next_state,priority)
    

if __name__== '__main__':
    start_grid = sgrid.SquareGrid([[1,2,3,4],[5,6,7,8],[9,0,10,12],[13,14,11,15]])
    solve(start_grid)