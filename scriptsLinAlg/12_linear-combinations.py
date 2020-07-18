#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
from auxfunctions.plotting import plot_vectors

v1 = np.array([2, 5])
v2 = np.array([3, 2])

v1v2 = 2*v1 + 1*v2

plot_vectors(v1,v2,v1v2, 
             colors=['red', 'blue', 'orange'], 
             ylimits=(-1,12))

scalars = np.arange(-10, 10)

plt.figure()
for a in scalars:
    for b in scalars:
        vector = a*v1 + b*v2
        plt.plot(*vector, 'b.', ms=2.5)


plt.axvline(color='gray')
plt.axhline(color='gray')
plt.xlim(-80, 80)
plt.ylim(-80, 80)
plt.show()