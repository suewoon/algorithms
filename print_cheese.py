#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 14:25:42 2017

@author: suewoonryu
"""
import colorful

def print_melting_cheese(self, board=None):
        if board is None:
            board = self.board

        print()
        print("—" * len(board[0]))
        for row in board:
            for e in row:
                if e == 0:
                    print(colorful.black(e), end=' ')
                elif e == 1:
                    print(colorful.yellow(e), end=' ')
                elif e == 6:
                    print(colorful.red('c'), end=' ')
                elif e == 7:
                    print(colorful.blue('h'), end=' ')
            print()
        print("—" * len(board[0]))