from methods.stack_methods import denoise, startracks, noise_extractor, untrack
import os
from processing.utils import generate_name


def stacking(dir, method):
    files = os.listdir(dir)
    files = list(map(lambda x: os.path.join(dir, x), files))
    files = list(filter(lambda x: x.endswith(".png"), files))

    if method == "denoise":
        img = denoise(files)
    elif method == "startracks":
        img = startracks(files)
    elif method == "noise extractor":
        img = noise_extractor(files)
    elif method == "untrack":
        img = untrack(files)

    name = generate_name()
    img.save(name)

    return [name]
