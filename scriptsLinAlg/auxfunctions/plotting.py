#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(*vectors, colors=['red', 'blue'], alpha=1, xlimits=(-1,8), ylimits=(-1,8)): 
    plt.figure()
    plt.axvline(x=0, color='gray', zorder=0)
    plt.axhline(color='gray', zorder=0)
    origin = [0,0]
    for i,vector in enumerate(vectors):
        x = np.concatenate([origin, vector] )
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy',
                   scale_units='xy',
                   scale=1,
                   color=colors[i],
                   alpha=alpha)
    plt.xlim(*xlimits)
    plt.ylim(*ylimits)


