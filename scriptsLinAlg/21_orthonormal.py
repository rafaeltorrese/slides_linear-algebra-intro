#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])

# Orthogonal by columns
print(A[:, 0].dot(A[:, 1]))
print(A[:, 0].dot(A[:, 2]))
print(A[:, 1].dot(A[:, 2]))

# Orthonormal by columns
print(np.linalg.norm(A[:, 0]))
print(np.linalg.norm(A[:, 1]))
print(np.linalg.norm(A[:, 2]))

# Do the same by each row

B = np.array([[np.cos(100), -np.sin(100)],
              [np.sin(100), np.cos(100)]])
print('\n', np.linalg.norm(B[:,0]))  # by column
print('\n', np.linalg.norm(B[:,1]))
print('\n', np.linalg.norm(B[0,:]))  # by row
print('\n', np.linalg.norm(B[1,:]))

print(B[:,0].dot(B[:,1]))  # Orthogonal
print(B[0].dot(B[1]))

Bt = B.T
Binv = np.linalg.inv(B)
