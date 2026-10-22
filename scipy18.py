from scipy.spatial.distance import euclidean

A = [2, 4, 6]
B = [5, 8, 10]

distance = euclidean(A,B)

print("euclidean distance: ",distance)