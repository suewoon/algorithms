#!/usr/local/bin python3
# solution for https://www.hackerrank.com/challenges/king-richards-knights

class Board(object):
    def __init__(self, n):
        # n*n board, value 0 ~ n*n-1
        self.board = [[i for i in range(j, j+n)] for j in range(0, n**2, n)]
        self.n = n
        self.cache = {}

    def rotate(self, a, b, d):
        original = [[self.board[i][j] for j in range(b, b+d+1)] for i in
                    range(a, a+d+1)]
    
        rotated = list(zip(*original[::-1]))
        for i in range(a, a+d+1):
            for j in range(b, b+d+1):
                self.board[i][j] = rotated[i-a][j-b]
        return

    def make_cache(self):
        for i in range(self.n):
            for j in range(self.n):
                self.cache[self.board[i][j]] = (i, j)
    
    def get_coord(self, k):
        coord = self.cache[k]
        return '{} {}'.format(coord[0]+1, coord[1]+1)


if __name__ == '__main__':
    n = int(input())
    s = int(input())
    board = Board(n)
    for i in range(s):
        a, b, d = map(int, input().split())
        board.rotate(a-1, b-1, d)
    board.make_cache()
    l = int(input())
    for i in range(l):
        val = int(input())
        print(board.get_coord(val))

