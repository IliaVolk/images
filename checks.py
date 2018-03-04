import numpy
from scipy.ndimage.interpolation import geometric_transform
from skimage.transform import rescale
from math import sqrt
from numba import jit, types
from steps.interleaving import interleaving
from skimage.io import imread
image = imread('1.jpg', as_grey=True)
image = rescale(image, 4)
print(image.shape)
size_diff = image.shape[0] * image.shape[1] / 25000
if size_diff > 1:
    image = rescale(image, 3/sqrt(size_diff))

print(image.shape)
