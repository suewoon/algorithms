#!/usr/bin/env python3
# pytest 

from baekjoon_11403 import Graph

class TestClass(object):
    def test_is_reachable(self):
        g = Graph(3)
        for string in '010\n001\n100'.split('\n'):
            g.make_graph(string)
        g.print_reachability_graph()
        assert g.reachability_graph[1][1] == 0

