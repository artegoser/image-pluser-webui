from PIL import Image, ImageFilter
from skimage import feature
import numpy as np

methods = ["Sharpen", "Edge detection", "Canny edge detection"]


def edge(file_name):
    image = Image.open(file_name)

    image = image.convert("L")

    return image.filter(ImageFilter.FIND_EDGES)


def canny_edge(file_name):
    image = Image.open(file_name)
    image = image.convert("L")
    image = np.asarray(image)

    return Image.fromarray(feature.canny(image, sigma=2))


def sharpen(file_name):
    image = Image.open(file_name)
    return image.filter(ImageFilter.SHARPEN)


methods_funcs = {
    "Sharpen": sharpen,
    "Edge detection": edge,
    "Canny edge detection": canny_edge,
}
