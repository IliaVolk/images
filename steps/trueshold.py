from numba import jit
import numpy

@jit
def trueshold(image):
    '''
    applies trueshold algorithm for given image
    :param image: numpy.ndarray
    :return: numpy.ndarray
    '''
    result = numpy.empty(image.shape)
    n, m = image.shape
    for i in range(n):
        for j in range(m):
            result[i,j] = 1 if image[i,j] > 0 else 0
    return result
