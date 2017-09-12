#!/usr/bin/env python3
#  solution for https://algospot.com/judge/problem/read/BOARDCOVER
import sys
input = sys.stdin.readline

class Board(object):
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.board = []
        self.cache = {} 
        self.blocks = [[(0, 0), (1, 0), (0, 1)], [(0, 0), (0, 1), (1, 1)],
                       [(0, 0), (1, 0), (1, 1)], [(0, 0), (1, 0), (1, -1)]]

    def read_line(self, string):
        line = []
        for char in string:
            if char == '#':
                line.append(1)
            elif char == '.':
                line.append(0)
        self.board.append(line)

    @staticmethod
    def to_string(board):
        return '\n'.join([''.join(['#' if e > 0 else '.' for e in row]) for row in board])
    
    def cover(self):
        board_to_cover = self.board[:]
        return self.cover_helper(board_to_cover)

    def cover_helper(self, board):
        def is_covered(board, x, y, block_type, revert):
            covered = True
            for i in range(3):
                ny = y + self.blocks[block_type][i][0]
                nx = x + self.blocks[block_type][i][1]
                if (ny < 0 or ny >= len(board) or nx <0 or nx >= len(board[0])):
                    covered  =  False
                elif (board[ny][nx]+revert) > 1:
                    covered =  False
                if not (ny < 0 or ny >= len(board) or nx <0 or nx >= len(board[0])):
                    board[ny][nx] += revert
            return covered

        available = False
        for i in range(self.h):
            for j in range(self.w):
                if board[i][j] == 0:
                    blank = (i, j)
                    available = True  # find a blank space
                    break
            else:
                continue
            break

        board_str = self.to_string(board)
        if board_str in self.cache:
            return self.cache[board_str]

        if not available:
            return 1
        elif available:
            ans = 0
            for block_type in range(4):
                if is_covered(board, blank[1], blank[0], block_type, 1):
                    # print(x,y,delta_1_x,delta_1_y,delta_2_x,delta_2_y)
                    ans += self.cover_helper(board)
                is_covered(board, blank[1], blank[0], block_type, -1)
                self.cache[self.to_string(board)] = ans
        return ans

def main():
    testcases = int(input())
    for i in range(testcases):
        (h, w) = tuple([int(x) for x in input().split()])
        b = Board(h, w)
        for i in range(h):
            b.read_line(input())
        print(b.cover())


if __name__ == '__main__':
    main()
