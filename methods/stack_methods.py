from PIL import Image, ImageChops
from tqdm import tqdm
import numpy as np


def denoise(files):
    images = [np.asarray(Image.open(file)) for file in tqdm(files)]
    return Image.fromarray(np.uint8(np.mean(images, axis=0)))


def startracks(files):
    image = Image.open(files[0])
    for file in tqdm(files):
        im2 = Image.open(file)
        im3 = ImageChops.lighter(image, im2)
        image = im3

    return image


def noise_extractor(files):
    image = Image.open(files[0])
    for file in tqdm(files, unit=" images"):
        im2 = Image.open(file)
        im3 = ImageChops.difference(image, im2)
        image = im3

    return image


def untrack(files):
    image = Image.open(files[0])
    for file in tqdm(files, unit=" images"):
        im2 = Image.open(file)
        im3 = ImageChops.darker(image, im2)
        image = im3

    return image
