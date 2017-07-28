# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:23:11 2017

@author: suewoonryu
"""
def optimalPath(x,y):
    #print("x : "+str(x)+" y: "+str(y))
    """
    find a optimal way from (0,0) to the bottom of the triangle where the sum of board[x][y] is the maximum
    :param x:
    :param y:
    :return: sum of the value through the path
    """
    if y == rows-1 :
        return triangle[y][x]
        
    if cache[y][x] != -1:
        return cache[y][x]
    ans = 0
    ans = triangle[y][x] + max(optimalPath(x,y+1),optimalPath(x+1,y+1))
    cache[y][x] = ans
    return ans
    
testcases = int(input())
for i in range(testcases):
    rows = int(input())
    triangle = []
    cache = [[-1]*rows for i in range(rows)]
    for j in range(rows):
        triangle.append([int(j) for j in input().split()])
    #rint(triangle)
    print(optimalPath(0,0))
    #print(cache)
