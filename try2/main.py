from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

from math import pi
from skimage.io import imread
from skimage.transform import radon, rescale, rotate
from skimage.color import rgb2gray
import numpy
import scipy.ndimage
from steps.autocorellation import autocorellation
from steps.interleaving import interleaving
from steps.twodfilter import twodfilter
from steps.trueshold import trueshold
from steps.xor import xor
from steps.diff import diff
from steps.log import log_mapping

# images = (imread('image.png', as_grey=True), imread('image2.png', as_grey=True))
images = [
    imread('../static/head.png', as_grey=True),
    imread('../static/lena.jpg', as_grey=True),
]

fig, axs = plt.subplots(2, len(images), figsize=(8, 4.5))
for i in range(len(images)):
    ax = axs[0]
    ax = ax[i]
    image = images[i]
    ax.set_title('Image {}'.format(i))

    ax.imshow(image, cmap=plt.cm.Greys_r, aspect='auto')

sing = []
for i in range(len(images)):
    ax = axs[1]
    ax = ax[i]
    image = images[i] * 255
    # theta = np.linspace(0., 180., max(image.shape), endpoint=False)
    # sinogram = radon(image, theta=theta, circle=True)
    sinogram = log_mapping(image)
    ax.imshow(sinogram, cmap=plt.cm.Greys_r, aspect='auto')

fig.tight_layout()
plt.show()
