#!/usr/bin/env python3 
# Longest Common Subsequence of two strings (sequential but not neccessarily
# contiguous) 

class LCS(object):
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def return_lcs(self):
        len_x = len(self.x)
        len_y = len(self.y) 
        seen = {}  #memoization

        def c(i, j):
            if (i, j) in seen : 
                return seen[(i, j)]
            elif i == len_x or j == len_y : 
                return 0 
            else : 
                res = 0
                for i in range(len_x):
                    for j in range(len_y):
                        if self.x[i] == self.y[j]:  #match
                            res = 1+c(i+1, j+1)
                        else:
                            res = max(c(i, j+1), c(i+1, j))
                seen[(i, j)] = res
                return res 
       
        
        return c(0,0)


def main():
    lcs = LCS('HIEROGLYPHOLOGY', 'MICHAELANGELO')
    print(lcs.return_lcs())


if '__name__' == '__main__':
    main()
