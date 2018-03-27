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
from scipy import fftpack
from numpy import abs, linspace
from cmath import sqrt
# images = (imread('image.png', as_grey=True), imread('image2.png', as_grey=True))
images = [
    imread('../static/text1.jpg', as_grey=True),
    imread('../static/cor.jpg', as_grey=True),
]

fig, axs = plt.subplots(5, len(images), figsize=(8, 4.5))
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
    ax2 = axs[2]
    ax2 = ax2[i]
    image = images[i]
    # theta = np.linspace(0., 180., max(image.shape), endpoint=False)
    #theta = linspace(0, 180, sqrt(2).real*image.shape[0])
    sinogram = image
    sinogram2 = autocorellation(sinogram)
    ax2.imshow(sinogram2, cmap=plt.cm.Greys_r, aspect='auto')
    ax.imshow(sinogram, cmap=plt.cm.Greys_r, aspect='auto')


fig.tight_layout()
plt.show()
