#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/coin-on-the-table/editorial


def get_min_flips(board, k, n, m):
    # goal:  도착 지점* 의 row, col
    d_row, d_col = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == '*':
                d_row = i; d_col = j;
                break
        else:
            continue
        break
     

    # flips: time k일때(0,0) - (i, j) 까지 오는데 필요한 최소 flip 수
    flips = [[[float('inf') for _ in range(m)] for _ in range(n)] for _ in
             range(k+1)]

    # k = 0 일때 coin은 무조건 (0,0)에 존재
    flips[0][0][0] = 0

    # 3d array flips 채우기
    for t in range(1, k+1):
        for i in range(n):
            for j in range(m):
                val = float('inf')
                if i-1 >= 0:
                    val = min(val, flips[t-1][i-1][j] + (0 if board[i-1][j] == 'D' else 1))
                if i+1 < n:
                    val = min(val, flips[t-1][i+1][j] + (0 if board[i+1][j] == 'U' else 1))
                if j-1 >= 0:
                    val = min(val, flips[t-1][i][j-1] + (0 if board[i][j-1] == 'R' else 1))
                if j+1 < m:
                     val = min(val, flips[t-1][i][j+1] + (0 if board[i][j+1] == 'L' else 1))
                flips[t][i][j] = val

    ans = float('inf')
    for t in range(k+1):
        ans = min(ans, flips[t][d_row][d_col])
    if ans == float('inf'):
        ans = -1
    return ans 


if __name__ == '__main__':
    (n, m, k) = map(int, input().split())
    board = []
    for row in range(n):
        board.append(list(input()))
    print(get_min_flips(board, k, n, m))
