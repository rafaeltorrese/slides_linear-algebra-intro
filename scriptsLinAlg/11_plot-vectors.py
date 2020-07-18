#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt
# from auxfunctions.plotting import plot_vectors

v1 = np.array([2, 5])
v2 = np.array([3,2])

def plot_vectors(vectors, colors, alpha=1): 
    plt.axvline(x=0, color='gray', zorder=0)
    plt.axhline(color='gray', zorder=0)
    for i in range(len(vectors)):
        x = np.concatenate([[0,0], vectors[i]] )
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy',
                   scale_units='xy',
                   scale=1,
                   color=colors[i],
                   alpha=alpha)
    # plt.xlim(*xlimits)
    # plt.ylim(*ylimits)
    
plot_vectors([v1,v2], ['blue', 'red'])
# plt.xlim(-1,8)
# plt.ylim(-1,8)