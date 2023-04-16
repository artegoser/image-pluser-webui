from PIL import Image, ImageChops
from tqdm import tqdm


def denoise(files):
    bias = 1
    image = Image.open(files[0])
    for file in tqdm(files):
        alpha = 1 / bias

        im2 = Image.open(file)
        im3 = Image.blend(image, im2, alpha)

        image = im3

        bias += 1

    return image


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
