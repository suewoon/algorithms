#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/grid-challenge


def sort_mat(mat, n):
    '''
    return whether the mat is able to be rearranged so that every row and 
    every column is lexicographically sorted
    '''
    for j in range(len(mat[0])):
        for i in range(0, n-1):
            if mat[i][j] > mat[i+1][j]:
                return False
    
    return True


if __name__ == '__main__':
    testcases = int(input())
    for i in range(testcases):
        mat = []
        n = int(input())
        for j in range(n):
            mat.append(sorted(input()))
        print('YES' if sort_mat(mat, n) else 'NO')

