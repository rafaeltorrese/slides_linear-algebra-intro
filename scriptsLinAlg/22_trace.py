#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np
mat = np.arange(1,10).reshape(3,3)
trace = np.trace(mat)
print(trace)