from PIL import Image, ImageFilter


def edge(file_name):
    image = Image.open(file_name)

    image = image.convert("L")

    return image.filter(ImageFilter.FIND_EDGES)


def sharpen(file_name):
    image = Image.open(file_name)
    return image.filter(ImageFilter.SHARPEN)
