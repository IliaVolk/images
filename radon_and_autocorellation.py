from skimage.io import imread, imsave
from skimage.transform import radon
from numpy import max
from steps.autocorellation import autocorellation

image = imread('static/lena.jpg', as_grey=True)
sinogram = radon(image)
auto = autocorellation(sinogram)

imsave('radon.png', sinogram/max(sinogram))
imsave('autocorellation.png', auto/max(auto))


