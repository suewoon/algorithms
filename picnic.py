# !/usr/bin/env
# makingPairs.py

import sys

areFriends = []
isTaken = []
numOfStudents = 0
#todo: read lines from input stream and call methods
def main():
    numberOfTrials = sys.stdin.readline()
    for i in range(0, numberOfTrials*2, 2):
        studentInfo = list(sys.stdin.readine()[:-1])
        numOfStudents = studentInfo[0]
        numOfFriendsPairs = studentInfo[1]
        friends = list(sys.stdin.readline()[:-1])
        for j in range(0, len(numOfFriendsPairs),2):
            x = friends[j]
            y = friends[j+1]
            if x>y :
                areFriends[y][x]=True
            else:
                areFriends[x][y] = True
        print(countingPairs(areFriends))

#todo : calculate and return a number of available pairs
def countingPairs(isTaken):
    # return unmatched one yet
    unmatched = -1
    for i in range(0,numOfStudents):
        if isTaken[i] is False :
            unmatched = i
            break

    #when everyone is matched
    if(unmatched == -1):
        return 1

    #num of possible pairs
    numOfPairs = 0

    for i in range(unmatched+1, numOfStudents):
        if isTaken[i] is False and areFriends[unmatched][i]:
            isTaken[unmatched] = isTaken[i] = True
            numOfPairs += countingPairs(isTaken)
            isTaken[unmatched] = isTaken[i] = False

    return numOfPairs


if __name__ == "__main__" : main()
