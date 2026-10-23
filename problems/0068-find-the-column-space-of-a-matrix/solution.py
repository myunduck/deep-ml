
import numpy as np

def matrix_image(A):
	# Write your code here
	arr = np.array(A)
	m, n = arr.shape

	basis_indices = []

	for j in range(n):
		test_indices = basis_indices + [j]
		sub_mat = arr[:, test_indices]

		if np.linalg.matrix_rank(sub_mat) > len(basis_indices):
			basis_indices.append(j)

	result_matrix = arr[:, basis_indices]

	return result_matrix.tolist()
	pass
