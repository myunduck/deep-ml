import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	A = []
	for row in a:
		for i in row:
			A.append(i)

	if len(A) != new_shape[0] * new_shape[1]:
		return []
		
	j = 0
	K = []
 
	for row in range(new_shape[0]):
		S = []
		K.append(S)

		for col in range(new_shape[1]):
			S.append(A[j])
			j += 1

	return K