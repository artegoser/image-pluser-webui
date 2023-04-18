from methods.stack_methods import (
    methods_funcs,
)
import os
from processing.utils import generate_name


def stacking(dir, method):
    files = os.listdir(dir)
    files = list(map(lambda x: os.path.join(dir, x), files))

    img = methods_funcs[method](files)

    name = generate_name()
    img.save(name)

    return [name]
