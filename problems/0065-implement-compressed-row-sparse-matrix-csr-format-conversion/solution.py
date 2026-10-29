import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""
	
	pointer = 0
	vals = []
	col_idx = []
	row_ptr = [0]
	
	for row in dense_matrix:
		col = 0
		for i in row:
			if i != 0:
				vals.append(i)
				col_idx.append(col)
				pointer += 1
			col += 1
		row_ptr.append(pointer)
		

	return vals, col_idx, row_ptr
	pass
