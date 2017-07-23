#!/usr/bin/env python3 
"""solution for https://www.acmicpc.net/problem/1018
"""

from pprint import pprint
import numpy as np 

class Board(object):
    def __init__(self,n,m):
        self.rows = n
        self.cols = m 
        self.original_board = []
        self.set_standard_case()

    def set_standard_case(self):
        line1 = [-1, 1, -1, 1, -1, 1, -1, 1]
        line2 = [1, -1, 1, -1, 1, -1, 1, -1]
        self.case1 = []
        self.case2 = []
        for i in range(8):
            if i%2 == 0 : 
                self.case1.append(line2)
                self.case2.append(line1) 
            else : 
                self.case1.append(line1)
                self.case2.append(line2)

    def create_board(self, string):
        line = []
        for char in list(string):
                if char == 'W':
                    line.append(-1)
                elif char == 'B':
                    line.append(1)
        self.original_board.append(line)

    def crop_board(self):
        changes=[[0]*(self.rows-7) for i in range(self.cols-7)]
        minum_changes = 64 
        for i in range(self.rows-7):
            for j in range(self.cols-7):
                changes[i][j] = self.sum(self.original_board[i:i+8][j:j+8])
                if changes[i][j] < minum_changes:
                    minum_changes = changes[i][j]

        return minum_changes


    def sum(self, cropped_board):
        sum1, sum2  = 0, 0
        sum1 = np.sum(np.subtract(self.case1,cropped_board))*0.5
        sum2 = np.sum(np.subtract(self.case2,cropped_board))*0.5
        return min(abs(sum1), abs(sum2)) 

    def print_board(self):
        pprint(self.cropped_board)


def main():
    m, n = [int(i) for i in input().split()]
    board = Board(n, m)
    for i in range(n):
        board.create_board(input())
    print(board.crop_board())

if __name__ == '__main__':
    main() 

