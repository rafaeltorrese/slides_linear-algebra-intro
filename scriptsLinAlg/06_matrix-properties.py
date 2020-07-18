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

C = np.array([
        [4, 1],
        [7, 3],
        ])

# Associative
ABC = A.dot(B.dot(C))
AB_C = A.dot(B).dot(C)


# Distributive
D = A.dot(B + C)
E = A.dot(B) + A.dot(C)

# Commutative
print('\n', B.dot(C))
print('\n', C.dot(B))
print('\n', B.dot(C) == C.dot(B))

v1 = np.array([[3],
               [8],
               [1],
                ])

v2 = np.array([[4],
               [8],
               [3],
               ])

print('\n', v1.T.dot(v2))
print('\n', v2.T.dot(v1))