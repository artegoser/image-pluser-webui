import gradio as gr
from processing.stacking import stacking


with gr.Blocks() as app:
    with gr.Tab("Stacking"):
        gr.Markdown("Stacking images.")
        with gr.Row():
            with gr.Column():
                directory = gr.Text(
                    placeholder="A directory with many images of the same size", lines=1, label="Directory")
                methods = gr.Dropdown(
                    choices=["denoise", "startracks", "noise extractor", "untrack"], value="denoise", label="Method")
                submit = gr.Button("Submit")

            with gr.Column():
                output = gr.Gallery()

            submit.click(stacking, inputs=[
                         directory, methods], outputs=[output])

    with gr.Tab("Bulk processing"):
        gr.Markdown(
            "Mass processing of images one at a time and saving to video if needed.   # **WIP, not working**")
        with gr.Row():
            with gr.Column():
                directory = gr.Text(
                    placeholder="A directory with many images of the same size", lines=1, label="Directory")
                methods = gr.Dropdown(
                    choices=["denoise", "startracks", "noise extractor", "untrack"], value="denoise", label="Method")
                submit = gr.Button("Submit")

    with gr.Tab("Video to images"):
        gr.Markdown(
            "Convert video to images.   # **WIP, not working**")
        with gr.Row():
            with gr.Column():
                video = gr.Video(label="Video")

                format = gr.Radio(
                    choices=["png", "jpg"], value="png", label="Format of image")
                submit = gr.Button("Submit")

    with gr.Tab("Images to video"):
        gr.Markdown("Convert images to video.   # **WIP, not working**")
        with gr.Row():
            with gr.Column():
                directory = gr.Text(
                    placeholder="A directory with many images of the same size", lines=1, label="Directory")

                fps = gr.Number(label="FPS")
                submit = gr.Button("Submit")


app.launch()
