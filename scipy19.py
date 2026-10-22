import numpy as np
from scipy.spatial.distance import pdist,squareform

points = np.array([[1, 2],
    [3, 4],
    [5, 1],
    [2, 6],
    [7, 3]])

distance = pdist(points)
print("distance between every pair of poinst:")
print(distance)

distance_matrix = squareform(distance)
print("\ndistance matrix: ")
print(distance_matrix)