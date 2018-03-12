import numpy as np
from numba import jit
from math import log, sqrt, atan2
from scipy.ndimage.interpolation import geometric_transform

'''@jit
def transform(coords, img, max_radius):
    # Put coord[1] in the interval, [-pi, pi]
    theta = 2 * np.pi * coords[1] / (img.shape[1] - 1.)

    # Then map it to the interval [0, max_radius].
    # radius = float(img.shape[0]-coords[0]) / img.shape[0] * max_radius
    radius = max_radius * coords[0] / img.shape[0]

    i = 0.5 * img.shape[0] - radius * np.sin(theta)
    j = radius * np.cos(theta) + 0.5 * img.shape[1]
    return i, j

@jit
def log_mapping(img):
    #Transform img to its polar coordinate representation
#
 #   order: int, default 1
  #      Specify the spline interpolation order.
   #     High orders may be slow for large images.
    # max_radius is the length of the diagonal
    # from a corner to the mid-point of img.
    max_radius = 0.5*np.linalg.norm( img.shape )



    polar = geometric_transform(img, transform, extra_arguments=(img, max_radius))

    return polar'''

@jit
def log_mapping(im):
    im1 = 1+im
    im2 = np.log(im1)
    return np.log(im2)
