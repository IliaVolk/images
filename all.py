from __future__ import print_function, division
from os import fork
import numpy as np
import matplotlib.pyplot
from datetime import datetime
from math import pi, sqrt
from skimage.io import imread, imsave, imshow
from skimage.transform import radon, rescale, rotate
from skimage.color import rgb2gray
import numpy
import scipy.ndimage
from steps.autocorellation import  autocorellation
from steps.interleaving import interleaving
from steps.twodfilter import twodfilter
from steps.trueshold import trueshold
from steps.xor import xor
from steps.diff import diff
from steps.log import log_mapping
from os import listdir, curdir, path

from numba import jit
import json

def main():

    results = []

    for i in range(len(images)):
        image = images[i]
        file = files[i]
        print('Handling file {}:{}'.format(i, file), image.shape)
        print('Starting radon', datetime.now())
        theta = np.linspace(0., 180., max(image.shape), endpoint=False)
        sinogram = radon(image, theta=theta, circle=True)
        print('Starting autocorellation', datetime.now())
        sinogram = autocorellation(sinogram)
        print('Starting to_polar', datetime.now())
        sinogram = log_mapping(sinogram)
        print('Starting fft2', datetime.now())
        sinogram = numpy.fft.fft2(sinogram)
        print('Starting interleaving', datetime.now())
        real, imaginary = interleaving(sinogram)
        print('Starting 2dfilter', datetime.now())
        real, imaginary = twodfilter(real), twodfilter(imaginary)
        print('Starting trueshold', datetime.now())
        real, imaginary = trueshold(real), trueshold(imaginary)
        print('Starting xor', datetime.now())
        sinogram = xor(real, imaginary)
        sign_file = 'sign_{}'.format(file)
        imsave('static/{}'.format(sign_file), sinogram)
        results.append({
            "image": file,
            "sign": sign_file,
            "sign_data": [x for x in sinogram.reshape((1, 400))[0]],
        })
    return results

if __name__ == '__main__':
    files = [f for f in listdir(path.join(curdir, 'static')) if (f.endswith('.jpg') or f.endswith('.png')) and not (f.startswith('sign_') or f.startswith('small_'))]
    print('working with files: {}'.format(files))
    images = [imread('static/{}'.format(f), as_grey=True) for f in files]
    results = main()

    f = open('static/result.js', 'w')
    f.write('const data = ')
    f.write(json.dumps(results))
