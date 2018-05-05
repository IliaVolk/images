from numba import jit
import numpy
@jit
def twodfilter(image):
    n, m = image.shape
    result = numpy.empty(image.shape)
    for i in range(n-1):
        for j in range(m-1):
            result[i,j] = -image[i][j]-image[i+1][j+1]+image[i+1][j]+image[i][j+1]
    return result
