#!/usr/bin/env/python3
#solution for https://algospot.com/judge/problem/read/WILDCARD
#Created on Fri Feb 10 00:13:21 2017


class Wildcard(object):
    def __init__(self, pattern):
        self.pattern = pattern

    def is_matched(self, string):
        len_pattern = len(self.pattern)
        len_str = len(string)

        #empty pattern can only match with empty string  
        if len_pattern == 0 :
            return len_str==0

        cache = [[False]*(len_pattern+1) for i in range(len_str+1)]
        cache[0][0] = True

        # pattern is null 
        for i in range(len_str+1):
            cache[i][0] = False

        #text is null 
        for j in range(1, len_pattern+1):
            if self.pattern[j-1] == '*':
                cache[0][j] = cache[0][j-1]
        #else 
        for i in range(1, len_str+1):
            for j in range(1, len_pattern+1):
                if self.pattern[j-1] == '*':
                    cache[i][j] = cache[i][j-1]
                elif self.pattern[j-1] == '?' or  self.pattern[j-1]==string[i-1]:
                    cache[i][j] = cache[i-1][j-1]
                else :
                    cache[i][j] = False 

        return cache[len_str-1][len_pattern-1] 


if __name__ == '__main__': 
    testcases = int(input())
    for i in range(testcases):
        pattern  = input() 
        wc = Wildcard(pattern)
        n_of_files = int(input())
        for j in range(n_of_files):
            file_name = input() 
            if wc.is_matched(file_name) : print(file_name)

