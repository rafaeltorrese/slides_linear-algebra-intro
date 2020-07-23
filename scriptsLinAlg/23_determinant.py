#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
from auxfunctions.plotting import plot_vectors

v1 = np.array([0, 1])
v2 = np.array([1, 0])

plot_vectors(v1,v2, xlimits=(-0.25, 2), ylimits=(-0.25, 2))

A = np.array([[2, 0],
              [0, 2]])

v1_transf = A.dot(v1)
v2_transf = A.dot(v2)

plot_vectors(v1_transf, v2_transf, colors=['orange', 'green'], 
             xlimits=(-0.25, 3), ylimits=(-0.25, 3))

A_det = np.linalg.det(A)
print('Determinant A:', A_det)
area_transf = abs(v1_transf[0] - v2_transf[0]) * abs(v1_transf[1] - v2_transf[1])
print('Transformed Area: ', area_transf)
B = A * [-1, 1]
B_det = np.linalg.det(B)
v1_transf = B.dot(v1)
v2_transf = B.dot(v2)
plot_vectors(v1_transf, v2_transf, v1, v2, 
             colors=['blue', 'red', 'orange', 'green'], 
             xlimits=(-2.5, 1.5), ylimits=(-0.5,2.5))