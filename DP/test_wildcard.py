#!/usr/bin/env/python3!
# pytest for wildcard.py

from wildcard import Wildcard 

def test_is_matched1():
    pattern = Wildcard('he?p')
    assert helper_test(pattern, ['help',
                                 'heap','helpp'])==[True, True , False]

def test_is_matched2():
    pass 

def helper_test(pattern, texts):
    ans = []
    for text in texts:
        if pattern.is_matched(text):
            ans.append(True)
        else:
            ans.append(False)
    return ans 
