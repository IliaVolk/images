import numpy as np
from scipy.ndimage.interpolation import geometric_transform
from numba import jit

@jit
def log_mapping(im):
    return np.log10(1 + im)
