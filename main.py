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
    imread('static/lena_rotate2.jpg', as_grey=True),
    imread('static/lena.jpg', as_grey=True),
    imread('static/lena_scale.jpg', as_grey=True),
    imread('static/lena_rotate180.jpg', as_grey=True),
    imread('static/lena_rotate10.jpg', as_grey=True),
    imread('static/lena_translate10.jpg', as_grey=True)
    # imread('11.jpg', as_grey=True),
    # imread('12.jpg', as_grey=True),
    # imread('13.jpg', as_grey=True),
    # imread('14.jpg', as_grey=True),
    # imread('15.jpg', as_grey=True),
    # imread('17.jpg', as_grey=True),
    # imread('18.jpg', as_grey=True),
    # imread('19.jpg', as_grey=True),
    # imread('110.jpg', as_grey=True)
    # imread('image1.png', as_grey=True),
    # imread('image11.png', as_grey=True),
    # imread('image111.png', as_grey=True)
]

'''images = [imread(im+'.jpg', as_grey=True) for im in [
    'c1', 'c2', 'c3', 'car1'
]]'''
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
    image = images[i]
    # theta = np.linspace(0., 180., max(image.shape), endpoint=False)
    # sinogram = radon(image, theta=theta, circle=True)
    sinogram = radon(image, circle=False)
    '''sinogram = autocorellation(sinogram)
    sinogram = log_mapping(sinogram)
    #sinogram = numpy.abs(numpy.fft.fft2(sinogram))
    #sinogram = numpy.log(sinogram)
    sinogram = numpy.fft.fft2(sinogram)
    real, imaginary = interleaving(sinogram)
    real, imaginary = twodfilter(real), twodfilter(imaginary)
    real, imaginary = trueshold(real), trueshold(imaginary)
    sinogram = xor(real, imaginary)
    #sinogram = sinogram / sinogram.max()
    ax.set_title(",".join(["diff({})={}".format(i, diff(item, sinogram)) for i, item in enumerate(sing)]))
    print(i, ",".join(["diff({})={}".format(i, diff(item, sinogram)) for i, item in enumerate(sing)]))
    # ax.imshow(sinogram)
    sinogram = numpy.array(sinogram)
    sing.append(sinogram)'''
    ax.imshow(sinogram, cmap=plt.cm.Greys_r, aspect='auto')

fig.tight_layout()
plt.show()
