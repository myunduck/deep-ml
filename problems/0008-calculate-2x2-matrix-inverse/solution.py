import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """

    # Your code here
    M = []
    for row in matrix:
        for i in row:
            M.append(i)

    det = M[0] * M[3] - M[1] * M[2] 
    if det == 0:
        return None

    indet = 1/det

    FM = np.array([[M[3], -M[1]],
            [-M[2], M[0]]])

    result = indet * FM
    return result.tolist()

    pass