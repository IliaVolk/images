from numba import jit

@jit
def diff(im1, im2):
    '''
    computes Hemming distance between 2 fingerprints
    :param im1: numpy.ndarray
    :param im2: numpy.ndarray
    :return: int
    '''
    res = 0
    m, n = im1.shape
    for i in range(m):
        for j in range(n):
            if im1[i][j] != im2[i][j]:
                res += 1
    return res