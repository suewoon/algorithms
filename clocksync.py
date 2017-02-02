# !/usr/bin/env
# clocksync.py

import sys

INF = 999
SWITCHES = 10
CLOCKS = 16

linked = [[3, 3, 3., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 3, 0., 0., 0., 3, 0., 3, 0., 3, 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 3, 0., 0., 0., 0., 0., 3, 0., 0.,
           0., 3, 3],
          [3, 0., 0., 3, 3, 3, 3, 0., 0., 0., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 3, 3, 3, 0., 3, 0., 3,
           0., 0., 0.],
          [3, 0., 3, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 3, 3],
          [0., 0., 0., 3, 0., 0., 0., 0., 0., 0., 0., 0., 0.,
           0., 3, 3],
          [0., 0., 0., 0., 3, 3, 0., 3, 0., 0., 0., 0., 0.,
           0., 3, 3],
          [0., 3, 3, 3, 3, 3, 0., 0., 0., 0., 0., 0., 0.,
           0., 0., 0.],
          [0., 0., 0., 3, 3, 3, 0., 0., 0., 3, 0., 0., 0.,
           3, 0., 0.]]


def main():
    testcases = sys.stdin.readline()
    print('Try %s times..', str(testcases))
    for line in sys.stdin():
        print(findMininum(list(line), 0))


if __name__ == "__main__": main()


def areAligned(clockboard):
    for i in range(0, 16):
        if clockboard[i] != 12:
            return False
    return True


def press(clockboard, switch):
    clockboard += linked[switch]
    for i in range(0, 16):
        if clockboard[i] == 15:
            clockboard[i] -= 3


def findMininum(clockboard, switch):
    if (switch == SWITCHES):
        return 0 if areAligned(clockboard) else INF
    minimumTimes = INF
    for i in range(0, 4):
        minimumTimes = min(minimumTimes, i + findMininum(clockboard, switch + 1))
        press(clockboard, switch)

    return minimumTimes
