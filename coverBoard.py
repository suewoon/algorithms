# !/usr/bin/env
# coverBoard.py

import sys

numOfTrials = sys.stdin.readline()
print('# of trials  {}'.format(numOfTrials))
info = sys.stdin.readline()
row = info.split(' ')[0]
col = info.split(' ')[1]
print('{}rows and {}cols'.format(row,col))
""
for i in range(0, row):
board = [[str(n) for n in line.split()] for line in sys.stdin.readlines()]


coverType = [[],[]]



 