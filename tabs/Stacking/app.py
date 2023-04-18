import gradio as gr
from processing.stacking import stacking
from methods.stack_methods import methods

with gr.Blocks() as app:
    gr.Markdown("Stacking images.")
    with gr.Row():
        with gr.Column():
            directory = gr.Text(
                placeholder="A directory with many images of the same size",
                lines=1,
                label="Directory",
            )
            method = gr.Dropdown(choices=methods, value=methods[0], label="Method")
            submit = gr.Button("Submit")

        with gr.Column():
            output = gr.Gallery()

        submit.click(stacking, inputs=[directory, method], outputs=[output])
