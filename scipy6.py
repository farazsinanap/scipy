import numpy as np
from  scipy.linalg import solve

A = np.array([[2,1],
              [1,-1]])
B = np.array([10,2])

solution = solve(A,B)

print("x =",solution[0])
print("y =",solution[1])