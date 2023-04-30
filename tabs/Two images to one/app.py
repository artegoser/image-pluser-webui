import gradio as gr
from processing.two_to_one import two_to_one
from methods.two_to_one_methods import methods

with gr.Blocks() as app:
    gr.Markdown("Get one image from two.")
    with gr.Row():
        with gr.Column():
            img1 = gr.Image()
            img2 = gr.Image()
            method = gr.Dropdown(choices=methods, value=methods[0], label="Method")
            submit = gr.Button("Submit")

        with gr.Column():
            output = gr.Gallery()

        submit.click(two_to_one, inputs=[img1, img2, method], outputs=[output])
