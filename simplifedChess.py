# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 02:43:49 2017

@author: suewoonryu
"""
#each player has exactly one queen, at most 2 rooks, at most 2 minor pieces is Bishpop, Knight

import sys 

def whiteWin():
    

testcases = int(input())
for i in range(testcases):
    (w,b,m) = sys.stdin.readline()[:-1].split(' ')
    w =int(w) 
    b =int(b)
    m =int(m)
    board = {} 
    for j in range(0, w):
        pos = input().split(' ')
        board[(pos[1],int(pos[2]))] = 'W'+pos[0]
    for k in range(0, b):
        pos = input().split(' ')
        board[(pos[1],int(pos[2]))] = 'B'+pos[0]
    if whiteWin():
        print('YES')
    else :
        print('NO')
    #print(board)
        