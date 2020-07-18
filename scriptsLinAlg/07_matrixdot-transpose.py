#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
A = np.array([
        [7,  1], 
        [2, -3], 
        [4,  8], 
    ])
  
B = np.array([
        [ 1, 6 ],
        [-2, 3 ],
        ])

AB_t = A.dot(B).T
print('\n AB_t\n', AB_t)

A_t = A.T
B_t = B.T
print('\n At\n', A_t)
print('\n Bt\n', B_t)

Bt_dot_At = B_t.dot(A_t) # swap A,B to B,A
print('\n', Bt_dot_At)

