from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.transform import radon, \
    rescale, EssentialMatrixTransform, matrix_transform
import skimage.filters

from numpy import array
image = imread("image.png", as_grey=True)
image = rescale(image, scale=0.4, mode='reflect')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

ax1.set_title("Original")
ax1.imshow(image, cmap=plt.cm.Greys_r)

theta = np.linspace(0., 180., max(image.shape), endpoint=False)
arr = array([[1, -1], [-1, 1]])
tr = EssentialMatrixTransform(matrix=arr)
sinogram = matrix_transform(image, tr)
ax2.set_title("Transform")
ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
           extent=(0, 180, 0, sinogram.shape[0]), aspect='auto')

fig.tight_layout()
plt.show()

