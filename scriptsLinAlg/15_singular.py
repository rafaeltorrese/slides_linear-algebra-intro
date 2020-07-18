#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np

A = np.array([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    ])

eigvalues, eigvectors= np.linalg.eig(A.T)
print(eigvalues == 0)

print(A[eigvalues == 0, :])

print((A[0] + A[1]) == A[2])
print((A[2] - A[0]) == A[1])
print((A[2] - A[1]) == A[0])

print(np.linalg.inv(A))