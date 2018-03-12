import numpy
from numba import jit

@jit
def autocorellation(image):
    result = numpy.empty(image.shape)
    m, n = image.shape
    for l in range(m):
        for tetha in range(n):
            s1 = 0.0
            s2 = 0.0
            for s in range(l, m):
                s2 += image[s, tetha]**2
                s1 += image[s, tetha]*image[s-l, tetha]
            if s2 == 0:
                print('div by zero')
            result[l,tetha] = s1 / s2 if s2 != 0 else 0
    return result
