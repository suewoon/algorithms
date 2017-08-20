#!/usr/bin/env python3 
# solution for https://www.acmicpc.net/problem/11403
class Graph(object):
    def __init__(self, d):
        self.d = d
        self.graph = []

    def make_graph(self,_string):
        self.graph.append([int(x) for x in _string])

    def is_reachable(self):
        """floyd-warshall"""
        reachability_graph = self.graph[:]
        for k in range(self.d):
            for i in range(self.d):
                for j in range(self.d):
                    if self.graph[i][k] ==1 and self.graph[k][j] ==1:
                        reachability_graph[i][j] =1
        return reachability_graph


    def print_reachability_graph(self):
        for row in self.is_reachable():
            print(' '.join(str(val) for val in row))

def main():
    d = int(input())
    graph = Graph(d)
    for i in range(d):
        _string = input().split()
        #print(_string)
        graph.make_graph(_string)
    graph.print_reachability_graph()

if __name__ == '__main__':
    main()
