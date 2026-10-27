import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""

#분모
	M = 0
	# Implement your code here
	mother = list(zip(v1, v2))
	for i in range(len(mother)):
		n = mother[i][0] * mother[i][1]
		M += n

#분자
	a = sum(i ** 2 for i in v1) ** 0.5
	b = sum(j ** 2 for j in v2) ** 0.5
	s = a*b

	return M/s 
	pass 