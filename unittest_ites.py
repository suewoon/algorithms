#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 22:25:04 2017
@author: suewoonryu
"""
from ites import ITESProblem
import unittest

class TestMyFuncions(unittest.TestCase):
    def setUp(self):
        self.p = ITESProblem()
        
    def test_getSignal(self):
        signal = self.p.getSignal()
        self.assertEqual(next(signal),1983)
        self.assertEqual(next(signal),8791)
        self.assertEqual(next(signal),4770)
        self.assertEqual(next(signal),7665)
        self.assertEqual(next(signal),3188)
    
    def test_count_subseq(self):
        self.assertEqual(self.p.countSubSeq(8791,20),1)
        self.assertEqual(self.p.countSubSeq(5265,5000),4)
        self.assertEqual(self.p.countSubSeq(3578452,5000000),1049)
    
    def tearDown(self):
        self.p = None
        
if __name__ == '__main__':
    unittest.main(exit=False)