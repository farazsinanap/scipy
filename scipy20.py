import numpy as np
from scipy.sparse import csr_matrix

matrix = np.array([[0, 0, 3],
                [0, 5, 0],
                [0, 0, 0]])

sparse_matrix = csr_matrix(matrix)

count = sparse_matrix.nnz

print("sparce matrix: ")
print(sparse_matrix)


print("number of non zero elements: ",count)