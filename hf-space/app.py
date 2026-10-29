# Crane Builder — Beryl Labs
# Hugging Face Space — Gradio SDK (RAW MODE)
# Serves crane-builder-ui.html as the IDE frontend

import gradio as gr
import pathlib

HTML_PATH = pathlib.Path(__file__).parent / "crane-builder-ui.html"

with gr.Blocks() as demo:
    gr.HTML(HTML_PATH.read_text(encoding="utf-8"))

if __name__ == "__main__":
    demo.launch()