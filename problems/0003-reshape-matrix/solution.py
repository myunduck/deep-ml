import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	A = [i for row in a for i in row]

	if len(A) != new_shape[0] * new_shape[1]:
		return []

	# for row in range(new_shape[0]):
	# 	S = []
	# 	K.append(S)

	# 	for col in range(new_shape[1]):
	# 		S.append(A[j])
	# 		j += 1

	n = list(new_shape)

	return [A[i:i+n[1]] for i in range(0, len(A), n[1])]
