import gradio as gr
from processing.bulk import bulk_processing

with gr.Blocks() as app:
    gr.Markdown(
        "Mass processing of images one at a time and saving to video if needed.   # **WIP, not working**"
    )
    with gr.Row():
        with gr.Column():
            directory = gr.Text(
                placeholder="A directory with many images.", lines=1, label="Directory"
            )
            method = gr.Dropdown(
                choices=["Edge detection", "Canny edge detection", "sharpen"],
                value="Sharpen",
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
