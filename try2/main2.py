from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

from math import pi
from skimage.io import imread
from skimage.transform import radon, rescale, rotate
from skimage.color import rgb2gray
import numpy
import scipy.ndimage
from steps.autocorellation import autocorrelation
from steps.interleaving import interleaving
from steps.twodfilter import twodfilter
from steps.trueshold import trueshold
from steps.xor import xor
from steps.diff import diff
from steps.log import log_mapping
from scipy import fftpack
from numpy import abs, linspace
from cmath import sqrt
import itertools
import os
# images = (imread('image.png', as_grey=True), imread('image2.png', as_grey=True))
images = [
    # *[imread(os.path.join('../static2', im), as_grey=True) for im in os.listdir('../static2')],
    #imread('../static/black_circle.jpg', as_grey=True),
    #imread('../static/black_circle_move.jpg', as_grey=True),
    #imread('../static/black_circle_scale.jpg', as_grey=True),

    imread('../static/lena.jpg', as_grey=True),
    imread('../static/lena_inv.jpg', as_grey=True),
    # imread('../static/lena_translate10.jpg', as_grey=True),
    imread('../static2/lena_yellow.jpg', as_grey=True),
    # imread('../static/lena_rotate90.jpg', as_grey=True),
    # imread('../static/lena_translate10_2.jpg', as_grey=True),
    # imread('../static/black_circle.jpg', as_grey=True),
]
def auto(a):
    a = numpy.fft.fft2(a)
    a = a * numpy.conj(a)
    a = numpy.fft.ifft2(a)
    a = numpy.fft.fftshift(a)
    a = numpy.real(a)
    a = a / numpy.max(numpy.max(a))
    return a

fig, axs = plt.subplots(4, len(images), figsize=(8, 4.5))
for i in range(len(images)):
    ax = axs[0]
    ax = ax[i]
    image = images[i]
    ax.set_title('Image {}'.format(i))

    ax.imshow(image, cmap=plt.cm.Greys_r, aspect='auto')

sign = []
for i in range(len(images)):
    ax = axs[1]
    ax = ax[i]
    ax2 = axs[2]
    ax2 = ax2[i]
    ax3 = axs[3]
    ax3 = ax3[i]
    image = images[i]
    sinogram1 = radon(image, circle=True)
    sinogram2 = autocorrelation(sinogram1)
    sinogram = log_mapping(sinogram2)
    sinogram = numpy.fft.fft2(sinogram)
    real, imaginary = interleaving(sinogram)
    real, imaginary = twodfilter(real), twodfilter(imaginary)
    real, imaginary = trueshold(real), trueshold(imaginary)
    sinogram = xor(real, imaginary)
    sign.append(sinogram)
    ax2.imshow(sinogram2, cmap=plt.cm.Greys_r, aspect='auto')
    ax.imshow(sinogram1, cmap=plt.cm.Greys_r, aspect='auto')
    ax3.imshow(sinogram, cmap=plt.cm.Greys_r, aspect='auto')

for (i, x), (j, y) in itertools.product(enumerate(sign), enumerate(sign)):
    print('diff', i, j, diff(x, y))
fig.tight_layout()
plt.show()
