#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  1 19:32:03 2017

@author: suewoonryu

solution for http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1113&sca=3030
"""

class Cheese(object): 
    def __init__(self, board, rows, cols):
        self.board = board 
        self.rows = rows 
        self.cols = cols 
    
    def mark_boundary(self,x,y):
        if self.board[x][y] == 0 : #치즈조각 바깥이면서 공기와 접촉인것을 9로 바꿈
            self.board[x][y]=9
            if x-1>=0:
                self.mark_boundary(x-1,y)
            
            if x+1<self.cols :
                self.mark_boundary(x+1,y)
            
            if y-1>=0:
                self.mark_boundary(x,y-1)
            
            if y+1<self.rows:
                self.mark_boundary(x,y+1)
    
def solve(board):
    board.mark_boundary(0,0)
    pieces = 0 
    while True : 
        for i in range(board.rows):
            for j in range(board.cols):
                if board[i][j] == 1:
                    if board[i-1][j]==9 or board[i+1][j]==9 or board[i][j]=-1:
                        pieces+=1
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]==9 or self.board[i][j]==-1:
                    self.board[i][j]=0
        if pieces==0:
            return 
        hours+=1
        
    return hours, pieces

if __name__ == "__main__": 
    board=[]
    (row, col) = tuple([int(i) for i in input().split()])
    for i in range(rows):
        board.append([int(i) for i in input().split()])
    cheese = Cheese(board,row,col)
    hours, pieces = solve(cheese)
    print(hours)
    print(pieces)
    
