import numpy as np

scalar = 5.679
A = np.array([
    [2, 4, -6, 7],
    [1, 3, 2, 1],
    [4,7,9,2]
    ]) 

B = np.array([
     [0, 1, 6, -2],
     [2, 3, 4, 3],
     [-2, 1, 4, 4]
     ])

C = A + B

print('\nMatrix Sum', C)

# Sum scalar to a matrix
print('\n', scalar + B)

print('\n', scalar * B)

