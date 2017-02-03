# !/usr/bin/env
# boggleGame.py

import sys

dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

def main():
    testcases = int(sys.stdin.readline())
    for i in range(0, testcases):
        board=[]
        for j in range(0,5):
            board.append(list(sys.stdin.readline())[:-1])
        givenWords = int(sys.stdin.readline())
        for k in range(0,givenWords):
            word = sys.stdin.readline()
            print(word)


#todo :  adjecent 8 characters from starting point (x,y)
def hasWord(x,y, word):

    if x not in range(0, len(word)) or y not in range(0,len(word)):
        return

    if board[x][y] != word[0]:
        return

    if(len(word)==1):
        print('find it! %s' %word)
        return True

    for i in range(8):
        if hasWord(x+dx[i],y+dy[i], word[1:]):
            return True

    return False


if __name__ = "__main__" : main()