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
        for k in range(1,self.d):
            for i in range(self.d):
                for j in range(self.d):
                    if 


    def print_reachability_graph(self):
        self.is_reachable(0)
        for row in self.reachability_graph:
            print(' '.join(str(val) for val in row))

def main():
    d = int(input())
    graph = Graph(d)
    for i in range(d):
        graph.make_graph(input())
    graph.print_reachability_graph()
