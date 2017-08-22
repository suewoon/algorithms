#!/usr/bin/env python3
#pytest for packing.py

from packing import KnapSack


class TestClass(object):
    def test_case0(self):
        ks = KnapSack(6, 10)
        for _string in "laptop 4 7\ncamera 2 10\nxbox 6 6\ngrinder 4 7\ndumbell 2 5\nencyclopedia 10 4".split('\n'):

            ks.add_item(_string.split(' '))
        print(ks.track_items())
        assert 0

    def test_case1(self):
        ks = KnapSack(6, 17)
        for _string in "laptop 4 7\ncamera 2 10\nxbox 6 6\ngrinder 4 7\ndumbell 2 5\nencyclopedia 10 4".split('\n'):
            ks.add_item(_string.split(' '))
        print(ks.track_items())
        assert 0

