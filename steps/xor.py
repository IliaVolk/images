from numba import jit
import numpy
@jit
def xor(image1, image2):
    m = len(image2)
    n = len(image2[0])
    result = numpy.empty((n, m))
    for i in range(n):
        for j in range(m):
            result[i, j] = int(bool(image1[i,j]) != bool(image2[i,j]))
    return result
