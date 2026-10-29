# Crane Builder — Beryl Labs
# Hugging Face Space — Static SDK
# Serves crane-builder-ui.html as the IDE frontend
# Connects to local model servers via CORS proxy (ports 11434/11437/11440)

from gradio import Blocks, HTML
import pathlib

HTML_PATH = pathlib.Path(__file__).parent / "crane-builder-ui.html"

with Blocks() as demo:
    HTML(HTML_PATH.read_text(encoding="utf-8"))

if __name__ == "__main__":
    demo.launch()
