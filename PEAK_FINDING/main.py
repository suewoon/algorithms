#!/usr/bin/env python3

import peak_algorithm_d2 as algorithm
from peak_problem_d2 import PeakProblem

def main():
    problemMatrix1 = [
            [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
            [ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
            [ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
            [ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
            [ 8,  9, 10, 11, 12, 11, 10,  9,  8,  7,  6],
            [ 7,  8,  9, 10, 11, 10,  9,  8,  7,  6,  5],
            [ 6,  7,  8,  9, 10,  9,  8,  7,  6,  5,  4],
            [ 5,  6,  7,  8,  9,  8,  7,  6,  5,  4,  3],
            [ 4,  5,  6,  7,  8,  7,  6,  5,  4,  3,  2],
            [ 3,  4,  5,  6,  7,  6,  5,  4,  3,  2,  1],
            [ 2,  3,  4,  5,  6,  5,  4,  3,  2,  1,  0]
    ]
    problemMatrix2 =  [[0,  0,  9,  0,  0,  0,  0],
                       [0,  0,  0,  0,  0,  0,  0],
                       [0,  1,  0,  0,  0,  0,  0],
                       [0,  2,  0,  0,  0,  0,  0],
                       [0,  3,  0,  0,  0,  0,  0],
                       [0,  5,  0,  0,  0,  0,  0],
                       [0,  4,  7,  0,  0,  0,  0],
                      ]

    problemMatrix = []
    problemMatrix.append(problemMatrix1)
    problemMatrix.append(problemMatrix2)

    for matrix in problemMatrix:
        problem = PeakProblem(matrix, (0, 0,len(matrix),len(matrix[0])))
        print('is a 2D peak? :',problem.isPeak(algorithm.attempt1(problem)))


if __name__ == '__main__':
    main()
