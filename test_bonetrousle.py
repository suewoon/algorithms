#!/usr/local/bin python3

from bonetrousle import solve, select

class TestCase(object):
    def test_case1(self):
        for string in '12 8 3\n10 3 3\n9 10 2\n9 10 2'.split('\n'):
            n, k, b = map(int, string.split())
            print(solve(n, k, b))
        assert 0

