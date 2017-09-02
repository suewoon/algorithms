#!/usr/bin/env python3
from baekjoon_2839 import Packing

class Test_Class(object):
    def test_measure(self):
        p = Packing()
        assert p.measure(18) == 4

