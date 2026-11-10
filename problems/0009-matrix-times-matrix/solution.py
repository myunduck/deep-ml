import numpy as np 
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    B = list(zip(*b))
    if len(a[0]) != len(B[0]):
        return -1

    c = np.dot(a,b)
    return c.tolist()