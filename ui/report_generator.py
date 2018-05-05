from skimage.io import imread, imsave
import numpy
from skimage.transform import radon

from steps.autocorellation import autocorellation
from steps.interleaving import interleaving
from steps.twodfilter import twodfilter
from steps.trueshold import trueshold
from steps.xor import xor
from steps.log import log_mapping
import os.path


def compare(data1, data2):
    diff = 0
    for d1, d2 in zip(data1, data2):
        if d1 != d2:
            diff += 1
    return diff



def generate_report(files, for_html=True):
    images = [imread(f, as_grey=True) for f in files]

    results = []

    for i in range(len(images)):
        image = images[i]
        file = files[i]
        sinogram = radon(image, circle=False)
        sinogram = autocorellation(sinogram)
        sinogram = log_mapping(sinogram)
        sinogram = numpy.fft.fft2(sinogram)
        real, imaginary = interleaving(sinogram)
        real, imaginary = twodfilter(real), twodfilter(imaginary)
        real, imaginary = trueshold(real), trueshold(imaginary)
        sinogram = xor(real, imaginary)
        sign_file = list(os.path.split(file))
        if for_html:
            sign_file = 'sign_{}'.format(sign_file[-1])
            imsave('static/' + sign_file, sinogram)
            results.append({
                "image": os.path.split(file)[-1],
                "sign": sign_file,
                "sign_data": [x for x in sinogram.reshape((1, 400))[0]],
            })
        else:
            results.append({
                'text': os.path.split(file)[-1],
                'image': os.path.abspath(file),
                'sign_data': [x for x in sinogram.reshape((1, 400))[0]],
                'diffs': [],
            })

    if not for_html:
        for d1 in results:
            for d2 in results:
                if d1 != d2:
                    diff = compare(d1['sign_data'], d2['sign_data'])
                    item = {
                        'text': '{} ({}%)'.format(d2['text'], diff/4),
                        'image': d2['image'],
                        'diffs': diff
                    }
                    d1['diffs'].append(item)
        for d in results:
            d['diffs'].sort(key=lambda x: x['diffs'])
    return results
