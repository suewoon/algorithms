# !/usr/bin/env
# boggleGame.py

import sys

dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

"""
    board will look like this
    [['U', 'R', 'L', 'P', 'M'], ['X', 'P', 'R', 'E', 'T'], ['G', 'I', 'A', 'E', 'T'], ['X', 'T', 'N', 'Z', 'Y'], ['X', 'O', 'Q', 'R', 'S']]
"""
board = []

#todo: read lines from input stream and call methods
def main():
    testcases = int(sys.stdin.readline())
    for i in range(0, testcases):
        for j in range(0, 5):
            board.append(list(sys.stdin.readline())[:-1])
        givenWords = int(sys.stdin.readline())
        word = []
        for k in range(0, givenWords):
            word.append(sys.stdin.readline()[:-1])
            for l in range(0, 5):
                for m in range(0, 5):
                    if (hasWord(l, m, word[k], board)):
                        print(word[k] + ' YES')
                        break
                else:
                    continue
                break


#todo: recursively find a word in the board
def hasWord(x, y, word, board):
    if x not in range(0, 5) or y not in range(0, 5):
        return False

    if board[x][y] != word[0]:
        return False

    if (len(word) == 1):
        return True

    for i in range(8):
        if hasWord(x + dx[i], y + dy[i], word[1:], board):
            return True

    return True


if __name__ == "__main__" : main()