#!/usr/bin/env python3 
# solution for : https://algospot.com/judge/problem/read/PICNIC

class MakingPairs(object):

    def __init__(self,n,l):
        self.n_of_students = n
        self.friends_pairs = l
        self.are_friends = [[False]*n for i in range(n)]
        self.check_friends()

    def check_friends(self):
        for i in range(0, len(self.friends_pairs), 2):
            id1 = self.friends_pairs[i]
            id2 = self.friends_pairs[i+1]
            if id1>id2 :
                self.are_friends[id2][id1]=True
            else :
                self.are_friends[id1][id2]=True

    def count_pairs(self):
        isTaken = [False]*self.n_of_students
        set_of_pairs = self.count_pairs_helper(isTaken)
        return set_of_pairs

    def count_pairs_helper(self,isTaken):
        available = -1
        for i in range(self.n_of_students):
            if not isTaken[i]:
                available = i
                break

        if available == -1:
            return 1

        ans = 0

        for partner in range(available+1, self.n_of_students):
            if not isTaken[partner] and not isTaken[available] and self.are_friends[available][partner]:
                isTaken[available] = isTaken[partner] = True
                ans += self.count_pairs_helper(isTaken)
                isTaken[available] = isTaken[partner] = False
        return ans

def main():
    test_cases  = int(input())
    for c in range(0, test_cases):
        (n,m)  = tuple(int(i) for i in input().split())
        friends_pairs = list(int(i) for i in input().split())
        mp = MakingPairs(n, friends_pairs)
        print(mp.count_pairs())

if __name__ == "__main__":
    main()
