import gradio as gr
from processing.bulk import video_to_images

with gr.Blocks() as app:
    gr.Markdown("Convert video to images.")
    with gr.Row():
        with gr.Column():
            video = gr.Video(label="Video")

        with gr.Column():
            format = gr.Radio(
                choices=["png", "jpg"], value="png", label="Format of image"
            )
            submit = gr.Button("Submit")
            submit.click(fn=video_to_images, inputs=[video, format])
