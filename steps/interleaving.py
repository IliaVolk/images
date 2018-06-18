from numba import jit, types
import numpy
from cmath import phase

@jit(types.UniTuple(types.float64[:,:], 2)(types.complex128[:,:]), nopython=True)
def interleaving(image):
    '''
    computes interleaving for given image
    :param image: numpy.ndarray
    :return: (numpy.ndarray, numpy.ndarray)
    '''
    n = 21
    image = image[:n,:n]
    magnitudes = numpy.empty((n, n))
    angles = numpy.empty((n, n))
    for i in range(n):
        for j in range(n):
            x = image[i, j].real
            y = image[i, j].imag
            # magnitudes[i, j] = x
            # angles[i, j] = y
            magnitudes[i,j] = numpy.sqrt(x**2 + y**2)
            angles[i,j] = phase(image[i, j])
    return magnitudes, angles
