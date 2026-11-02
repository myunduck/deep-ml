import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T = np.array(T)
	S = np.array(S)

	try:
		RT = np.linalg.inv(T)
		RS = np.linalg.inv(S)
	except:
		return -1

	F = np.dot(RT, A)

	return np.dot(F, S)