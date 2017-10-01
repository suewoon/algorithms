#!/usr/local/bin python3

from bonetrousle import solve

class TestCase(object):
    def test_case1(self):
        for string in '12 8 3\n10 3 3\n9 10 2\n9 10 2'.split('\n'):
            n, k, b = map(int, string.split())
            print(solve(n, k, b))
        assert 0

    def test_case2(self):
        for string in '69 9 6\n1000000000000000000 20 10\n210 20 20'.split('\n'):
            n, k, b = map(int, string.split())
            print(solve(n, k, b))
        assert 0

    def test_case3(self):
        for string in '155 20 10\n55 20 10\n1 1 1\n209 20 20\n211 20 20'.split('\n'):
            n, k, b = map(int, string.split())
            print(solve(n, k, b))
        assert 0

    def test_case4(self):
        for string in '1 20 1\n1 2 1\n154 20 10\n56 20 10\n156 20 10\n54 20 10'.split('\n'):
            n, k, b = map(int, string.split())
            print(solve(n, k, b))
        assert 0




