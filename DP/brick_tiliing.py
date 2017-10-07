#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/brick-tiling/problem


cache = {}
bricks = [[(0,0), (0,1), (0,2), (1,0)], [(0,0), (0,1), (0,2), (1,2)], 
          [(0,0), (1,0), (1,1), (1,2)], [(0,0), (1,0), (1,-1), (1,-2)],
          [(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (1,1), (2,1)],
          [(0,0), (0,1), (1,0), (2,0)], [(0,0), (1,0), (2,0), (2,-1)]]


def check_col(board, h, w, j):
    for i in range(h):
        if board[i][j] == '.':
            return False
    return True

def check_row(board, h, w, i):
    for j in range(w):
        if board[i][j] == '.':
            return False
    return True

def getiStart(board, h, w):
    for i in range(h):
        if check_row(board, h, w, i) == False:
            return i
    return h

def getjStart(board, h, w):
    for j in range(w):
        if check_col(board, h, w, j) == False:
            return j
    return w

def get_hash(board, r, c):
    '''
    make hash out of 2D array, since array is not hashable 
    '''
    istart = getiStart(board, r, c)
    jstart = getjStart(board, r, c)
    return str([x[jstart:] for x in board[istart:]])

def cover(i, j, k, board, uncover):
    '''
    cover or uncover the board (i,j) is top-left position of L shape brick
    '''
    for (x, y) in bricks[k]:
        if not uncover:
            board[i+x][j+y] = 'x'
        else:
            board[i+x][j+y] = '.'
    return board 


def check_bound(r, c, i, j, k, board):
    '''
    check whether L shape is out of bound or already marked 
    '''
    for (x, y) in bricks[k]:
        if (i+x) not in range(r) or (j+y) not in range(c) or board[i+x][j+y] != '.':
            return False
    return True 

def print_board(board):
    for line in board:
        print(line)
        
def tiling(r, c, i, j, board):
    '''
    return how many L bricks can be filled in the given board 
    L brick - 3 units on one side and 2 units on another 
    '''
    hash_val = get_hash(board, r, c)
    if hash_val in cache:
        return cache[hash_val]
    
    count = 0 
    for k in range(8):
        if check_bound(r, c, i, j, k, board):
            board = cover(i, j, k, board, False) # cover
            count += find_next(board, r, c, i, j)
            count %= 1000000007
            board = cover(i, j, k, board, True) # uncover
     
    cache[hash_val] = count 
    return count

def find_next(board, r, c, iprev, jprev):
    for i in range(iprev, r):
        jstart = 0
        if i == iprev: jstart = jprev
        for j in range(jstart, c):
            if board[i][j] == '.':
                return tiling(r, c, i, j, board)
    return 1

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        r, c = map(int, input().split())
        board = []
        for _r in range(r):
            board.append(list(input()))
        print(find_next(board, r, c, 0, 0))
