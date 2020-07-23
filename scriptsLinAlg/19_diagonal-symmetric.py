#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np

vector = np.array([1, 2, 3, 4, 5])
D = np.diag(vector)
print('\n', D[:4, :3])  # Non-symmetric
print('\n', D[:3, :4])  

A = np.diag([2, 3, 4, 5])
v1 = np.array([1, 1, 1, 1])

print('\n', A.dot(v1))

Ainv = np.diag(1/np.diag(A))
print('\n', A.dot(Ainv))

# Symmetric Matrix
print('\n', A.T)
print('\n', A)

sym_mat = np.array([
    [1, 2, 3],
    [2, -1, 7],
    [3, 7, 11]
    ])
print('\n', sym_mat)
print('\n', sym_mat.T)

