#!/usr/bin/env
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from auxfunctions.plotting import plot_vectors

def plot_space(v1,v2, scalars, xlimits=(-25,25), ylimits=(-25,25)):
    plt.figure()
    for a in scalars:
        for b in scalars:
            vector = a*v1 + b*v2
            plt.plot(*vector, 'b.', ms=2.5)
    plt.axvline(color='gray')
    plt.axhline(color='gray')
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)
    plt.show()


def plot_space3d(v1,v2, scalars, xlimits=(-25,25), ylimits=(-25,25)):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for a in scalars:
        for b in scalars:
            vector = a*v1 + b*v2
            ax.scatter(*vector, color='blue')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
    
    
# R1  as subspace of R2
v1 = np.array([1,1])
v2 = np.array([-1,-1])
scalars = np.arange(-10, 10)
plot_space(v1,v2,scalars)
plot_vectors(v1,v2, xlimits=(-2,2), ylimits=(-2,2))

# R2
v1 = np.array([1,0])
v2 = np.array([2,-3])
plot_vectors(v1,v2, colors=['orange', 'cyan'], xlimits=(-2,2), ylimits=(-4,2))
plot_space(v1,v2,scalars)


# R3
v1 = np.array([1, 0, 0])
v2 = np.array([2, -3, 0])
plot_space3d(v1,v2, scalars)

