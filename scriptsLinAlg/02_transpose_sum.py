#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
import numpy as np

scalar = 5.679
# define array
vector = np.array([
            [1, 2, 3],
            [1, 2, 3]
            ])

print(f'\n{vector}')
print(f'\n{vector.shape}')
vector_tranpose = vector.T
print(f'\nVector Transposed: \n{vector_tranpose}')
print('\n', vector_tranpose.shape)

tensor = np.array([
                    [[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]],
                    [[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]],
                    [[5, 78, 2, 34, 0], [6, 79, 3, 35, 1], [7, 80, 4, 36, 2]]
                    ])
print(f'\n{tensor}')
print(f'\n{tensor.shape}')
print(f'\n{tensor.ndim}')
tensor_t = tensor.T
print(f'\n{tensor_t}')
print(f'\n{tensor_t.shape}')
print(f'\n{tensor_t.ndim}')


