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

#분자
	S = 0
	#Implement your code here
	son = list(zip(v1, v2))
	for i in range(len(son)):
		s = son[i][0] * son[i][1]
		S += s

#분모
	a = sum(i ** 2 for i in v1) ** 0.5
	b = sum(j ** 2 for j in v2) ** 0.5
	M = a*b

	return S/M
	pass 