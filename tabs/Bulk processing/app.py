import gradio as gr
from processing.bulk import bulk_processing
from methods.bulk_methods import methods

with gr.Blocks() as app:
    gr.Markdown("Mass processing of images one at a time.")
    with gr.Row():
        with gr.Column():
            directory = gr.Text(
                placeholder="A directory with many images.", lines=1, label="Directory"
            )
            method = gr.Dropdown(
                choices=methods,
                value=methods[0],
                label="Method",
            )

            with gr.Accordion("Advanced settings", open=False) as acc:
                out_dir = gr.Text(
                    label="Output directory",
                    placeholder="The directory where the processed photos will be saved. If not specified `./output/images`",
                )
            submit = gr.Button("Submit")
            submit.click(
                fn=bulk_processing,
                inputs=[directory, out_dir, method],
            )
