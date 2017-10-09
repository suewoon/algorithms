#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/knightl-on-chessboard

from collections import deque 

def find(a, b, n):
    '''
    Print exactly n-1  lines of output in which each line i  contains n-1 
    space-separated integers describing the minimum number of moves knight(i,j)
    must make for each respective j. If some knight(i,j)  cannot reach position , print -1
    instead.
    '''
    def get_neighbor(current):
        (i, j) = current 
        neighbors  = [(i+a, j+b), (i+a, j-b), (i-a, j+b), (i-a, j-b),
                      (i+b, j+a), (i+b, j-a), (i-b, j+a), (i-b, j-a)]
        neighbors = filter(lambda x:x[0]<=n and x[0]>=0 and x[1]<=n and x[1]>=0, neighbors)
        return neighbors 
    
    def track_path(came_from):
        if (n,n) not in came_from:
            return -1
        path = []
        last_cell = (n, n)
        while last_cell != (0,0):
            path.append(last_cell)
            last_cell = came_from[last_cell]
            
        return len(path)
    
    s = (0,0)
    came_from = {(0, 0):None}
    frontier = deque([(0,0)])
    while frontier:
        current = frontier.pop()
        if current == (n, n):
            came_from
            break
        for neighbor in get_neighbor(current):
            if neighbor not in came_from:
                came_from[neighbor] = current
                frontier.extendleft([neighbor])
                
    #print(came_from)
    return track_path(came_from)


def get_moves(n):
    ans = [[-1 for _ in range(n-1)] for _ in range(n-1)]
    for i in range(1, n):
        for j in range(i, n):
            ans[i-1][j-1] = find(i, j, n-1)
            if i!=j : ans[j-1][i-1] = ans[i-1][j-1]
    for row in ans:
        print(' '.join([str(x) for x in row]))

if __name__ == '__main__':
    n = int(input())
    get_moves(n)
