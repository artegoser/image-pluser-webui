import gradio as gr

with gr.Blocks() as app:
    gr.Markdown(
        "Convert video to images.   # **WIP, not working**")
    with gr.Row():
        with gr.Column():
            video = gr.Video(label="Video")

            format = gr.Radio(
                choices=["png", "jpg"], value="png", label="Format of image")
            submit = gr.Button("Submit")
