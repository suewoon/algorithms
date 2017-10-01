#!/usr/local/bin/python3

from sherlock_and_anagrams import sherlockAndAnagrams

class TestClass(object):
    def test_case1(self):
        assert sherlockAndAnagrams('abba') == 4
        assert sherlockAndAnagrams('abcd') == 0
    
    def test_case2(self):
        assert sherlockAndAnagrams('ifailuhkqq') == 3
        assert sherlockAndAnagrams('hucpoltgty') == 2
        assert sherlockAndAnagrams('ovarjsnrbf') == 2
        assert sherlockAndAnagrams('pvmupwjjjf') == 6
        assert sherlockAndAnagrams('iwwhrlkpek') == 3




        


