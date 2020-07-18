#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import numpy as np

scalar = 5.679
vector = np.array([4, 6, 2])
mat = np.array([[3, 5],
                [1, 6],
                [9, 3]])

print(mat, vector)

# A = mat + vector  # Error

A = mat.T + vector

print('\nBroadcasting:\n', A)
print('\n', mat + 2 )

B = np.array([[2], 
              [2], 
              [2]])  # Column vector

print(f'\n{mat + B}')