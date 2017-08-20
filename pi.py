#!/usr/bin/env python3
#  solution for https://algospot.com/judge/problem/read/PI

import numpy as np

class PiFraction(object):
    def __init__(self):
        pass

    def diff(self, _list, degree=1):
        ans =  [(_list[i+1]-_list[i]) for i in range(len(_list)-1)]
        if degree == 1:
            return ans
        else :
            return self.diff(ans)

    def get_difficulty(self, subList):
        if len(subList) == 0:
            return 0
        """
        if self.cache[int(''.join(subList))] :
            return self.cache[int(''.join(subList))]
        """
        if all(self.diff(subList, 1) == 0):
            return 1

        if all(self.diff(subList, 1) == 1) or  all(self.diff(subList,1) == -1) :
            return 2

        if all(abs(self.diff(subList,1)) == abs(subList[1]-subList[0])) :
            return 4

        if all(self.diff(subList, 2) == 0):
            return 5

        return 10

    def min_difficulty(self, _list): 
        """
        return minumum difficulty of the given list 
        make the sublist of which length is 3 ~ 5 and calculate get the 
        difficulty then recursively call the function
        """
        if len(_list) <= 5:
            return self.get_difficulty(_list)
        else:
            ans = float('inf')
            for i in range(3, 6):
                ans = min(self.min_difficulty(_list[:i])+self.min_difficulty(_list[i:]), ans)
            return ans


def main():
    testcases = int(input())
    for i in range(testcases):
        _list = list(int(x) for x in input())
        fraction = PiFraction()
        print(fraction.min_difficulty(_list))


if __name__ == '__main__':
    main()
