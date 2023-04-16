import gradio as gr
from processing.bulk import images_to_video

with gr.Blocks() as app:
    gr.Markdown("Convert images to video.   # **WIP, not working**")
    with gr.Row():
        with gr.Column():
            directory = gr.Text(
                placeholder="A directory with many images of the same size", lines=1, label="Directory")

            fps = gr.Number(label="FPS")
            submit = gr.Button("Submit")

    submit.click(
        fn=images_to_video,
        inputs=[directory, fps],
    )
