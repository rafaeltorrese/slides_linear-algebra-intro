#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
y = 3x + 5
y = 2x + 3

. 3x 2 7y 5 25
4x 2 3y 5 22
'''

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5,5 , 20)

y1 = 3 * x + 5
y2 = 2 * x + 3


# plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)

# x axis limits and y axis limits
plt.xlim(-5, 5)
plt.ylim(-5, 5)

# axvline; vertical, axhline: horizontal
plt.axvline(0, color='gray') 
plt.axhline(0, color='gray')

# plt.show()

A = np.array([[-3, 1], 
              [-2, 1]])
print('\n', A)

b = np.array([5, 3])

sol1 = np.array([-2, -1])
print('\n', sol1)

print('\n', A.dot(sol1))
