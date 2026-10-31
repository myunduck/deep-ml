def compressed_col_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix into its Compressed Column Sparse (CSC) representation.

	:param dense_matrix: List of lists representing the dense matrix
	:return: Tuple of (values, row indices, column pointer)
	"""
	m = zip(*dense_matrix)
	vals = []
	row_inx = []
	col_ptr =[]
	c = 0

	for i in m:
		r = 0
		col_ptr.append(c)
		for j in i:
			if j != 0:
				vals.append(j)
				row_inx.append(r)
				c+= 1
			r += 1

	col_ptr.append(c) 

	return vals, row_inx, col_ptr
	pass
