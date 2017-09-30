#!/bin/local/bin/python3
from journey_to_the_moon  import Graph

class TestCases(object):
    def test_case1(self):
        graph = Graph(5, 3)
        graph.add_node(0,1)
        graph.add_node(2,3)
        graph.add_node(0,4)
        graph.dfs()
        assert graph.get_pairs(0) == 6


    def test_case2(self):
        graph = Graph(4, 1)
        graph.add_node(0, 2)
        graph.dfs()
        assert graph.get_pairs(0) == 5


    def test_case3(self):
        graph = Graph(1000, 1)
        graph.add_node(1, 2)
        graph.dfs()
        assert graph.get_pairs(0) == 499499
