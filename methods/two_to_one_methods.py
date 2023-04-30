from skimage.exposure import match_histograms
import numpy as np
from PIL import Image


def histogram_matching(img1, img2):
    return Image.fromarray(match_histograms(img1, img2, channel_axis=-1))


methods_funcs = {"Histogram matching": histogram_matching}

methods = list(methods_funcs.keys())
