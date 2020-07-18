#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import  numpy as np
# np.set_printoptions(suppress=True)

A = np.array([[1, 1, 2],
              [2, 4, -3],
              [3, 6, -5]])

b = np.array([9, 0, 1], dtype=np.float64)
Ainv = np.linalg.inv(A)
x = Ainv.dot(b)

c = np.array([3,6,1], dtype=np.float64)

