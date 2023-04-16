import gradio as gr
from processing.stacking import stacking

with gr.Blocks() as app:
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
