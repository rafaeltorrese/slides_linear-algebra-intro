#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt


v1 = np.array([0, 0, 2, 2])
v2 = np.array([0, 0, 2, -2])

plt.quiver([v1[0], v2[0]],
           [v1[1], v2[1]],
           [v1[2], v2[2]],
           [v1[3], v2[3]],
           angles='xy',
           scale_units='xy',
           scale=1,
           )

plt.axvline(color='gray')
plt.axhline(color='gray')
plt.xlim(-1,3)
plt.ylim(-3,3)
plt.show()

v1 = np.array([2, 2])
v2 = np.array([2, -2])
print('\n Orthogonal\n', v1.dot(v2.T))  # Orthogonal

print('\n', np.linalg.norm(v1))   # If Norm is 1, vectors are orthonormal
print('\n', np.linalg.norm(v2))

v1 = np.array([1,0])
v2 = np.array([0, -1])
print(v1.dot(v2.T))
print('\n', np.linalg.norm(v1))
print('\n', np.linalg.norm(v2))