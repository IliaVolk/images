from __future__ import print_function, division
from skimage.io import imread, imsave
from skimage.transform import radon

from steps.autocorellation import  autocorellation
from steps.interleaving import interleaving
from steps.twodfilter import twodfilter
from steps.trueshold import trueshold
from steps.xor import xor
from steps.log import log_mapping
from os import listdir, curdir, path
from scipy import fftpack
import json

def main():

    results = []

    for i in range(len(images)):
        image = images[i]
        file = files[i]
        sinogram = radon(image, circle=False)
        sinogram = autocorellation(sinogram)
        sinogram = log_mapping(sinogram)
        sinogram = fftpack.fft(sinogram)
        real, imaginary = interleaving(sinogram)
        real, imaginary = twodfilter(real), twodfilter(imaginary)
        real, imaginary = trueshold(real), trueshold(imaginary)
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
    images = [imread('static/{}'.format(f), as_grey=True) for f in files]
    results = main()

    f = open('static/result.js', 'w')
    f.write('const data = ')
    f.write(json.dumps(results))
