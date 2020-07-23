#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import  seaborn as sns

v1 = np.array([1,2,0, 5, 6, 0])
print('\n Zero Norm: ', np.linalg.norm(v1, ord=0))
v2 = np.array([1,-1,1,-1,1])
print('\n Norm One: ', np.linalg.norm(v2, ord=1))
v3 = np.array([4,3])
print('\n Euclidean Norm', np.linalg.norm(v3, ord=2))
print(np.linalg.norm(v3, ord=2)**2)
print(v3.dot(v3))

plt.quiver([0, 0, 4],
           [0, 0, 0],
           [4, 4, 0],
           [3, 0, 3],           
           angles='xy',
           scale_units='xy',
           scale=1,
           color=sns.color_palette()
           )
plt.axvline(color='gray')
plt.axhline(color='gray')
plt.xlim(-1,6)
plt.ylim(-1,6)
plt.show()
v4 = np.array([1,3, -100])
print('\n Norm L-Inf = ', np.linalg.norm(v4, ord=np.inf) )
