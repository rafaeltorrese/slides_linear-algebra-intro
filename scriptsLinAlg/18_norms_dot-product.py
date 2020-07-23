#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

v1 = np.array([0,3])
v2 = np.array([3,3])

# v1 = np.array([0,1])
# v2 = np.array([1,0])

plt.quiver([0,0],
           [0,0],
           [v1[0], v2[0]],
           [v1[1], v2[1]],
           scale_units='xy',
           angles='xy',
           scale=1,
           color=sns.color_palette(),
           )
plt.axhline(color='gray', alpha=0.6)
plt.axvline(color='gray', alpha=0.6)
plt.xlim(-2,6)
plt.ylim(-2,6)
plt.show()

v1tv2 = v1.T.dot(v2)
print(v1tv2)
result = np.linalg.norm(v1, ord=2) * np.linalg.norm(v2, ord=2) * np.cos(np.deg2rad(45))
print(result)
