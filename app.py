import datetime
import gradio as gr
from PIL import Image, ImageChops
import os
from tqdm import tqdm


def impluser(dir, method):

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


def generate_name():
    # if not exists output create it
    if not os.path.exists("./output"):
        os.mkdir("./output")

    return f"./output/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"


def denoise(files):
    bias = 1
    image = Image.open(files[0])
    for file in tqdm(files):

        alpha = 1/bias

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
    for file in tqdm(files, unit=' images'):
        im2 = Image.open(file)
        im3 = ImageChops.difference(image, im2)
        image = im3

    return image


def untrack(files):
    image = Image.open(files[0])
    for file in tqdm(files, unit=' images'):
        im2 = Image.open(file)
        im3 = ImageChops.darker(image, im2)
        image = im3

    return image


with gr.Blocks() as app:
    with gr.Row():
        with gr.Column():
            directory = gr.Textbox(
                placeholder="A directory on the same machine where the server is running.", lines=1, label="Directory")
            methods = gr.Dropdown(
                choices=["denoise", "startracks", "noise extractor", "untrack"], value="denoise", label="Method")
            submit = gr.Button("Submit")

        with gr.Column():
            output = gr.Gallery()

        submit.click(impluser, inputs=[directory, methods], outputs=[output])

app.launch()
