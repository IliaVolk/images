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
    #imread('../static/text1.jpg', as_grey=True),
    #imread('../static/text2.jpg', as_grey=True),
    imread('../static/lena.jpg', as_grey=True),
    imread('../static/lena_harshness.jpg', as_grey=True),
    imread('../static/lena_rotate180.jpg', as_grey=True),
    #imread('../static/lena_translate10.jpg', as_grey=True),
    #imread('../static/lena_translate10_2.jpg', as_grey=True),
    #imread('../static/lena_rotate10.jpg', as_grey=True),
    #imread('../static/lena_rotate10_noblack.jpg', as_grey=True),
    #imread('../static/lena_square.jpg', as_grey=True),
    #imread('../static/baboon_rotate180.jpg', as_grey=True),
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
    ax3 = axs[3]
    ax3 = ax3[i]
    ax4 = axs[4]
    ax4 = ax4[i]
    image = images[i]
    # theta = np.linspace(0., 180., max(image.shape), endpoint=False)
    #theta = linspace(0, 180, sqrt(2).real*image.shape[0])
    sinogram = radon(image, circle=False)
    print(1, sinogram.shape)
    sinogram2 = autocorellation(sinogram)
    print(2, sinogram2.shape)
    sinogram3 = log_mapping(sinogram2)
    print(3, sinogram3.shape)
    sinogram4 = numpy.fft.fft2(sinogram3)
    # sinogram4 = fftpack.fft2(sinogram3)
    print(4, sinogram4.shape)
    real, imaginary = interleaving(sinogram4)
    real, imaginary = twodfilter(real), twodfilter(imaginary)
    real, imaginary = trueshold(real), trueshold(imaginary)
    sinogram4 = xor(real, imaginary)
    ax2.imshow(sinogram2, cmap=plt.cm.Greys_r, aspect='auto')
    ax3.imshow(sinogram3, cmap=plt.cm.Greys_r, aspect='auto')
    ax.imshow(sinogram, cmap=plt.cm.Greys_r, aspect='auto')
    ax4.imshow(sinogram4, cmap=plt.cm.Greys_r, aspect='auto')


fig.tight_layout()
plt.show()
