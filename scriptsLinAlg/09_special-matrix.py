#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
# np.set_printoptions(suppress=True)

I = np.eye(4)  # Identity Matrix
vector = np.array([2,3,5,7])
print('\n', I)
print('\n', I.dot(vector))

A = np.array([[-3, 1], 
              [-2, 1]])

# Inverse
Ainv = np.linalg.inv(A)
print('\n', A)
print('\n', Ainv)
print('\n', A.dot(Ainv))

# Singular Matrix
B = np.array([[1,1], [1,1]])
# print(np.linalg.inv(B))