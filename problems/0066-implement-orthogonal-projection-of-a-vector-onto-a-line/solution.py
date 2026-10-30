
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot_vL= sum(v_i * l_i for v_i, l_i in zip(v, L))
	dot_ll= sum(l_i * l_i for l_i in L)

	scalar = dot_vL / dot_ll

	projection = [(scalar * l_i) for l_i in L]
	return projection
	pass
