# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:49:50 2017

@author: suewoonryu
"""
import sys 

def jump(x,y):
    #if cache has key (x,y) -> pass / if not put a vavlue in it 
    #base case n1 : out of range
    if x > n-1 or y > n-1 :
        return False 
    if x == n-1 and y == n-1 :
        return True 
        
    if (x,y) in cache:
        return cache[(x,y)]
    else :
        step = int(board[x][y])
        ans = jump(x + step, y) or jump(x, y+step)
        cache[(x,y)] = ans
        return ans
    


testcases = int(input())
for i in range(testcases):
    n = int(input())
    board=[]
    cache = {}
    for j in range(n):
        board.append(sys.stdin.readline()[:-1].split(' '))
    print(board)
    if(jump(0,0)):
        print('YES')
    else:
        print('NO')
        


