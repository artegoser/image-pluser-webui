import gradio as gr
from processing.bulk import images_to_video

with gr.Blocks() as app:
    gr.Markdown(
        "Mass processing of images one at a time and saving to video if needed.   # **WIP, not working**")
    with gr.Row():
        with gr.Column():
            directory = gr.Text(
                placeholder="A directory with many images of the same size", lines=1, label="Directory")
            methods = gr.Dropdown(
                choices=["denoise", "startracks", "noise extractor", "untrack"], value="denoise", label="Method")
            submit = gr.Button("Submit")
