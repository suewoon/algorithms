#!/usr/bin/env python3
#  solution for https://algospot.com/judge/problem/read/BOARDCOVER

import sys
input = sys.stdin.readline

class Board(object):
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.board = []
        self.blocks = [[(0, 0), (1, 0), (0, 1)],[(0, 0), (0, 1), (1, 1)],
                       [(0, 0), (1, 0), (1, 1)],[(0, 0), (1, 0), (1, -1)]]
    
    def make_board2(self, _string):
        self.board.append(list(_string))
    
    def make_board(self):
        for input_ in range(self.h):
            self.board.append(list(input())[:-1])
        print(self.board)
    
    def cover(self):
        board_to_cover = self.board[:]
        return self.cover_helper(board_to_cover)
    
    def cover_helper(self, board):
        available = False
        
        for i in range(self.h):
            for j in range(self.w):
                if board[i][j] == '.':
                    blank = (i, j)
                    available = True
                    break
            else :
                continue
            break
    
        if not available:
            return 1
        elif available:
            ans = 0
            for block_type in self.blocks:
                x, y = blank[0], blank[1]
                delta_1_x, delta_1_y = block_type[1][0], block_type[1][1]
                delta_2_x, delta_2_y = block_type[2][0], block_type[2][1]
                if x+delta_1_x >= 0 and y+delta_1_y >=0 and x+delta_2_x >=0 and y+delta_2_y >=0 and x+delta_1_x < self.h and x+delta_2_x < self.h and y+delta_1_y <self.w and y+delta_2_y <self.w and board[x+delta_1_x][y+delta_1_y]== board[x+delta_2_x][y+delta_2_y]=='.' :
                    #  print(x,y,delta_1_x,delta_1_y,delta_2_x,delta_2_y)
                    #  self.print_board(board)
                    board[x][y] = board[x+delta_1_x][y+delta_1_y] = board[x+delta_2_x][y+delta_2_y] = '#'
                    ans += self.cover_helper(board)
                    #  self.print_board(board)
                    board[x][y] = board[x+delta_1_x][y+delta_1_y] = board[x+delta_2_x][y+delta_2_y] = '.'
    
        return ans

def main():
    testcases = int(input())
    for i in range(testcases):
        (h, w) = tuple([int(x) for x in input().split()])
        b = Board(h, w)
        b.make_board()
        print(b.cover())


if __name__ == '__main__':
    main()
