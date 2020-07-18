#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import numpy as np
scalar = 5.679
vector = np.array([1,2,3])
mat = np.array([
                [1, 2],
                [3, 4]
                ])
tensor = np.array([
                    [[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]],
                    [[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]],
                    [[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]]
                    ])
print(scalar)
#print(scalar.shape)  # Error
print(f'Vector shape: {vector.shape}')
print(f'Matrix shape {mat.shape}')
print(f'Matrix dimension: {mat.ndim}')
print(f'\nTensor shape: {tensor.shape}')
print(f'Tensor dimensions: {tensor.ndim}')
print(len(vector))
print(len(mat))
print(f'\nMatrix size {mat.size}')
print(f'\nTensor Size: {tensor.size}')
