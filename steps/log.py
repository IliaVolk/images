from numpy import array, zeros, abs, sum, log
from numba import jit
from math import log, exp
import numpy
'''
divider = 100
@jit
def transform(i, j):
    a = exp(log(90).real / divider)
    i = int(log(1 + i, a))
    return i, j

@jit
def log_mapping(img):
    a = exp(log(90).real / divider)
    i = int(log(img.shape[0], a).real)
    res = zeros((i+1, img.shape[1]+1))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            coords = transform(i, j)
            res[coords] = img[i, j] / 2 + res[coords] / 2 \
                if res[coords] else img[i, j]

    res2 = []
    for row in res:
        if 0 != sum(abs(row)):
            res2.append(row)
    return array(res2)
    #return numpy.log(1 + array(res2))
'''

k0 = 0.001
@jit
def log_mapping(im):
    return k0*numpy.log(1 + im/k0)

