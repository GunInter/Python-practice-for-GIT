import numpy as np


# inputs first!
m = int(input('Pls enter value: m'))
n = int(input('Pls enter value: n'))
k = int(input('Pls enter value: k'))

# now m and n exist, so we can use them
A = np.random.randint(0, 2, (m, n))
B = np.random.randint(0, 2, (n, k))
