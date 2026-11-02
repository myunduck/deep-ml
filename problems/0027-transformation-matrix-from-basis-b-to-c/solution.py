import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	c = np.array(C)
	R = np.linalg.inv(c)
	b = np.array(B)
	T = np.dot(R, b)
	return T.tolist()