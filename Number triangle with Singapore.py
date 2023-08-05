# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 16:17:05 2021

@author: Pei Ren
"""

for i in range(1,10):
    print(' '*(10-i), end='')
    if (i == 5):
        print("SINGAPORE", end='')
    else:
        for j in range (1, i):
            print(j, end='')
        for j in range (i, 0, -1):
            print(j, end='')
    print('\n')