#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np

scalar = 5.678

vector = np.array([5,7])

mat = np.array([[4, 8],
                [1, 9],
                [3, 7]])

print('Vector shape', vector.shape)
print('Matrix shape', mat.shape)
print()
A = mat * vector
print('mat x vector \n', A)

B = mat.dot(vector)
print('\nDot Product \n', B)
print('\n', B.shape)