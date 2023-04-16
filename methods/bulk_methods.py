from PIL import Image, ImageFilter


def canny_edge(file_name):
    image = Image.open(file_name)

    image = image.convert("L")

    return image.filter(ImageFilter.FIND_EDGES)
