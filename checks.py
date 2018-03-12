import numpy
from scipy.ndimage.interpolation import geometric_transform
from skimage.transform import rescale
from math import sqrt
from numba import jit, types
from steps.interleaving import interleaving
from skimage.io import imread
image = imread('static/.jpg', as_grey=True)
image = rescale(image, 4)

