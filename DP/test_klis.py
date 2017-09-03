#/usr/bin/env python3
# pytest

from klis import KLIS

class Test_Class(object):
    def test_return_lis(self):
        klis = KLIS([9, 2])
        klis.read_input('1 9 7 4 2 6 3 11 10')
        print(klis.return_lis())
        assert 0

    def test_return_lis2(self):
        klis = KLIS([8, 4])
        klis.read_input('2 1 4 3 6 5 8 7')
        print(klis.return_lis())
        assert 0

    def test_return_lis3(self):
        klis = KLIS([8, 2])
        klis.read_input('5 6 7 8 1 2 3 4')
        print(klis.return_lis())
        assert 0



