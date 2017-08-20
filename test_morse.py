#!/usr/bin/env python3
# pytest for morse.py

from morse import Morse


class TestClass(object):
    def test_case1(self):
        morse = Morse(2, 2, 4)
        assert morse.k_th_code() == 'o--o'

    def test_case5(self):
        morse = Morse(2, 2, 5)
        assert morse.k_th_code() == 'o-o-'

    def test_case3(self):
        morse = Morse(6, 4, 1)
        assert morse.k_th_code() == '------oooo'

    def test_case4(self):
        morse = Morse(6, 4, 210)
        assert morse.k_th_code() == 'oooo------'

    def test_case6(self):
        morse = Morse(2,3,2)
        assert morse.k_th_code() == '-o-oo'

    def test_case2(self):
        morse = Morse(4, 8, 13)
        :assert morse.k_th_code() == '--o-ooo-oooo'
