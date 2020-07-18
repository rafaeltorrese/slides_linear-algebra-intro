#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np

A = np.array([[2, 0, -3],
              [4, 1,  5],])

B = np.array([[7, -1, 4, 7],
              [2, 5, 0, -4],
              [-3, 1, 2, 3],])

AB = A.dot(B)

# BA = B.dot(A)  # Error