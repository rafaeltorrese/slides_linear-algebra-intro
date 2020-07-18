#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

v1 = np.array([2, 7])
v2 = np.array([3,5])

v1v2 = v1 + v2

v1v2norm = np.linalg.norm(v1v2)

# triangle inequality
v1norm = np.linalg.norm(v1)
v2norm = np.linalg.norm(v2)
print(v1v2norm <= (v1norm + v2norm))
print(v1norm + v2norm)
v0 = np.array([0,0])

plt.quiver([v0[0], v0[0], v1[0]],
           [v0[0], v0[0], v1[1]],
           [v1[0], v1v2[0], v2[0]],
           [v1[1], v1v2[1], v2[1]],
           angles='xy',
           scale_units='xy',
           scale=1,
           color=sns.color_palette())

plt.axhline(color='gray')
plt.axvline(color='gray')
plt.xlim(-1,7)
plt.ylim(-1,14)
plt.show()

