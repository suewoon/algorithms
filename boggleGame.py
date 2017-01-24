# !/usr/bin/env
# boggleGame.py

import os
import numpy as np

"""board= [['N','N','N','N','S'],['N','E','E','E','N'],
         ['N','E','Y','E','N'],['N','E','E','E','N'],
         ['N','N','N','N','N']]"""

inputFile = open(os.path.join('input1.txt', os.getcwd()),'r')
data = [[str(n)] for n in line.split()] for line in inputFile
lines = inputFile.readlines()
board = np.array(' ',5*5)
numOfTrials = lines[0]
lines = lines[1:]
for i in range(0, numOfTrials):
    for i in (0,24):
        board[i] = lines[]
    testWords = lines[5]
    lines=lines[6+testWords:]

dx = [-1,-1,-1,1,1,1,0,0]
dy = [-1,0,1,-1,0,1,-1,1]

def hasWord(x,y, word):

    if x not in range(0, len(word)) or y not in range(0,len(word)):
        print('Out of Range')
        return

    if board[x][y] != word[0]:
        print('Could not find')
        return

    if(len(word)==1):
        print('find it! %s' %word)
        return True

    for i in range(8):
        if hasWord(x+dx[i],y+dy[i], word[1:]):
            return True

    return False

hasWord(2,2,'YES')
