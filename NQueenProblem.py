# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:45:17 2017

@author: suewoonryu
"""


class NQueenProblem(object):
    """
    given n*n board place n queens on this board so that 
    they don't attack each other. Finding any placement 
    of queens which do not attack each other. Once find out
    the solution, return the solution.
    """

    class Position(object):
        def __init__(self, row, col):
            self.row = row
            self.col = col
        def __repr__(self):
            return '('+str(self.row)+','+str(self.col)+')'

    def solveNQueen(self, N):
        position = [None]*N
        assert (N >= 1 and 13 >= N)
        hasSolution = self.solveNQueenUtil(N, 0, position)
        if hasSolution:
            return position
        else:
            print('no feasible solution')
            return []

    def solveNQueenUtil(self, N, row, positions):
        if row == N:
            return True

        for col in range(N):
            foundSafe = True
            for queen in range(row):
                if positions[queen].col == col or (positions[queen].row - positions[queen].col) == row - col or (positions[queen].row + positions[queen].col) == row + col:
                    foundSafe = False
                    break

            if foundSafe:
                positions[row] = self.Position(row, col)
                if self.solveNQueenUtil(N, row + 1, positions):
                    return True

        return False


N = int(input())
s = NQueenProblem()
positions = s.solveNQueen(N)
print(positions)
