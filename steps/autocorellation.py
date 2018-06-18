import numpy
from numba import jit


@jit
def autocorrelation(image):
    '''
    :param image: numpy.ndarray
    :return: npumpy.ndarray
    computes autocorrelation by y axis for given image
    '''
    result = numpy.empty(image.shape)
    m, n = image.shape
    for tetha in range(n):
        s2 = 0.0
        for s in range(m):
            s2 += image[s, tetha] ** 2
        for l in range(m):
            s1 = 0.0
            for s in range(l, m):
                s1 += image[s, tetha]*image[s-l, tetha]
            result[l, tetha] = s1 / s2 if s2 != 0 else 0
    return result
