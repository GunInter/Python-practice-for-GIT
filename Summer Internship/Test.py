import numpy as np


# inputs of the matrix dimensions :)
m = int(input('Pls enter value m:'))
n = int(input('Pls enter value n:'))
k = int(input('Pls enter value k:'))

# now m and n exist, so we can use them
A = np.random.randint(0, 2, (m, n))
B = np.random.randint(0, 2, (n, k))

# check if the inner dimensions match for multiplication
print("A shape:", A.shape)