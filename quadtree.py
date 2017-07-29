#!/usr/bin/env python3
#  solution for  https://algospot.com/judge/problem/read/QUADTREE

import sys
input = sys.stdin.readline

class QuadTree(object):
    def __init__(self, string):
        self.quadtree = string
    
    def up_side_down(self):
        if len(self.quadtree) == 1:
            return self.quadtree
        else:
            
            def up_side_down_helper(quadtree):
                
                if quadtree[0] == 'b' or quadtree[0] =='w':
                    ans = quadtree[0]
                    quadtree = quadtree[1:]
                    return ans
                else:
                    quadtree = quadtree[1:]
                
                q1 = up_side_down_helper(quadtree)
                #print(quadtree[:])
                q2 = up_side_down_helper(quadtree[len(q1):])
                #print(quadtree[len(q1):])
                q3 = up_side_down_helper(quadtree[len(q1)+len(q2):])
                #print(quadtree[len(q1)+len(q2):])
                q4 = up_side_down_helper(quadtree[len(q1)+len(q2)+len(q3):])
                #print(quadtree[len(q1)+len(q2)+len(q3):])
                
                return 'x' + q3 + q4 + q1 + q2
            
            return up_side_down_helper(self.quadtree)


def main():
    testcases = int(input())
    for i in range(testcases):
        qt = QuadTree(input())
        print(qt.up_side_down())

if __name__ == '__main__':
    main() 
