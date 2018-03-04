import numpy
from numba import jit, types

@jit
def autocorellation(image):
    result = numpy.empty(image.shape)
    m, n = image.shape
    for l in range(m):
        for tetha in range(n):
            s1 = 0.0
            s2 = 0.0
            for s in range(l, m):
                s1 += image[s, tetha]**2
                s2 += image[s, tetha]*image[s-1, tetha]

            result[l,tetha] = s1 / s2 if s2 != 0 else 1
    return result