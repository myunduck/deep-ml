def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here

	A = []

	for row in matrix:
		n = []
		for i in row:
			n.append(i * scalar)
	
		A.append(n)

	return A
	pass