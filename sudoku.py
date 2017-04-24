#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 07:40:10 2017

@author: suewoonryu

sudoku : arrange 1 to 9 with no repeats in row, col, or block 
"""

class Sudoku(object):
    def __init__(self):
        self.board = [] 
        self.make_board()
        self.row= 0
        self.col=0
        
    def solve(self):
        if not self.find_empty_location() :
            return True 
        for digit in range(1,10):
            if self.is_free_of_conflict(self.row, self.col, digit):
                self.update_board_location(self.board, self.row,self.col,digit)
                if self.solve(): return True # if it works out, done 
                self.update_board_location(self.row,self.col,0) #unmake 
        return False
    def find_empty_location(self,row=0,col=0):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col]== 0 : 
                    self.col = col 
                    self.row = row 
                    return True     
        return False 
    
    def update_board_location(self,row,col,digit):
        self.board[row][col] = digit 
                  
    def is_free_of_conflict(self, row,col,digit):
        if digit in self.board[row]: return False 
        for i in range(9):
            if self.board[i][col]==digit : return False 
        
        row_edge = int(row/3)*3 
        col_edge = int(col/3)*3 
        for i in range(row_edge, row_edge+3):
            for j in range(col_edge,col_edge+3):
                if self.board[i][j] == digit : return False
            
        return True
    def make_board(self):  
        for i in range(9):
            self.board.append(list(input()))

        
sudoku = Sudoku()
sudoku.solve()