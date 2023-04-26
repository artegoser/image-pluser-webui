from PIL import Image, ImageFilter
from skimage import feature
import numpy as np


def edge(file_name):
    image = Image.open(file_name)
    image = image.convert("L")
    return image.filter(ImageFilter.FIND_EDGES)


def canny_edge(file_name):
    image = Image.open(file_name)
    image = image.convert("L")
    image = np.asarray(image)

    return Image.fromarray(feature.canny(image, sigma=2))


def blur(file_name):
    image = Image.open(file_name)
    return image.filter(ImageFilter.BLUR)


def grayscale(file_name):
    image = Image.open(file_name)
    return image.convert("L")


def sharpen(file_name):
    image = Image.open(file_name)
    return image.filter(ImageFilter.SHARPEN)


methods_funcs = {
    "Sharpen": sharpen,
    "Edge detection": edge,
    "Canny edge detection": canny_edge,
    "Grayscale": grayscale,
    "Blur": blur,
}

methods = list(methods_funcs.keys())
