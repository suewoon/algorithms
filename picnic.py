# !/usr/bin/env
# makingPairs.py

import os
import numpy as np

inputFile = open(os.path.join(os.getcwd(),'input.txt'),'r')

#todo: read lines from inputFile and calculate the number of available pairs
lines = inputFile.readlines()

numberOfTrials = lines[0]

for i in range(1, 1+numberOfTrials*2, 2):
    N = lines[i].split(' ')[0]
#    numOfPairs = lines[i].split(' ')[1]
    board = np.array(0, N*N).reshape(N,N)
    for j in range(0,len(lines[i+1].split(' ')),2):



def countingPairs(isMatched):
    pointer = -1
    for i in range(0,len(isMatched)):
        if(!isMatched[i]):
            pointer = i
            break

    if(pointer == -1):
        return

    for i in range(pointer+1, len(isMatched)):
        if(board[pointer])

    return numOfPairs
