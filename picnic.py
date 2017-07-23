#!/usr/bin/env python3 
#solution for : https://algospot.com/judge/problem/read/PICNIC


def main():
    test_cases  = int(input())
    for i in range(0, testcases*2):
        1st_line = list(int(i) for i in input())
        2nd_line  = list(int(i) for i in input())
        mp = MakingPairs(1st_line[0],1st_line[1],2nd_line)
        print(mp.count_friend_pairs())

class MakingPairs(object):
    def __init__(self,n,m,l):
        self.n_of_students = n
        self.n_of_friends_pairs = m
        self.friends_pairs = l
        self.are_friends = [[False]*n for i in range(n)]

    def check_they_are_friends(self):
        for i in range(0,len(self.are_friends),2):
            id1 = self.friends_pairs[i]
            id2 = self.friends_pairs[i+1] 
            if id1>id2 : 
                self.are_friends[id2][id1]=True 
            else :
                self.are_friends[id1][id2]=True 

    #todo : count  a number of pairs if they're friends
    def count_friend_pairs(self):
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

        return numOf Pairs


if __name__ == "__main__" : main()
