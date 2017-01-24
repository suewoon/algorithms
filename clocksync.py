# !/usr/bin/env
# clocksync.py

from sys import stdin
import numpy as np

INF = 999, SWITCHES = 10, CLOCKS = 16

linked = [[ 3,  3,  3.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.],
       [ 0.,  0.,  0.,  3,  0.,  0.,  0.,  3,  0.,  3,  0.,  3,  0.,
         0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  3,  0.,  0.,  0.,  0.,  0.,  3,  0.,  0.,
         0.,  3,  3],
       [ 3,  0.,  0.,  3,  3,  3,  3,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  3,  3,  3,  0., 3,  0.,  3,
         0.,  0.,  0.],
       [ 3,  0.,  3,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  3,  3],
       [ 0.,  0.,  0.,  3,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  3,  3],
        [ 0.,  0.,  0.,  0.,  3,  3,  0.,  3,  0.,  0.,  0.,  0.,  0.,
         0.,  3,  3],
       [ 0.,  3,  3,  3,  3,  3,  0.,  0.,  0.,  0.,  0.,  0.,  0.,
         0.,  0.,  0.],
       [ 0.,  0.,  0.,  3,  3,  3,  0.,  0.,  0.,  3,  0.,  0.,  0.,
         3,  0.,  0.]]

clockboard = np.zeros(16)
print(clockboard)

def areAligned(clockboard):
    for i in range(0,16):
        if clockboard[i]!=12:
            return False
    return True

def press(clockboard, switch):
        clockboard+=linked[switch]
        for i in range(0,16):
            if clockboard[i] == 15:
                clockboard[i] -= 3

#switch는 다음에 누를 스위치 번호
def findMininum(clockboard, switch):
    pressedSwitch=0

    if areAligned():
        return pressedSwitch

    for i in range(0,4):

        press(clockboard,switch)
        pressedSwitch = findMininum(clockboard,switch+1)

for trial in range(0,numOfTrials):
    clockboard = [[int(n) for n in line.split('')] for line in stdin.readline()]
    print(clockBoard)
    solve(cl)



numOfTrials = int(stdin.readline())
print('# of trials : %s'%numOfTrials)

