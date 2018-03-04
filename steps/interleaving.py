from numba import jit, types
import numpy


@jit(types.UniTuple(types.float64[:,:], 2)(types.complex128[:,:]), nopython=True)
def interleaving(image):
    n = 20
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
            angles[i,j] = numpy.arctan2(y, x)
    return magnitudes, angles