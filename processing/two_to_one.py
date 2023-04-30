from methods.two_to_one_methods import methods_funcs
from processing.utils import generate_name


def two_to_one(img1, img2, method):
    img = methods_funcs[method](img1, img2)
    out_path = generate_name(subfolder="two_to_one")
    img.save(out_path)

    return [out_path]
