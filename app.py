import gradio as gr
from processing.stacking import stacking
import sys
import importlib
import pathlib
import os
import copy
from tabs import tabs

tabs_dir = pathlib.Path(__file__).parent / "tabs"


all_tabs = []
tab = None
for tab_name in tabs:
    old_path = copy.deepcopy(sys.path)
    sys.path = [os.path.join(tabs_dir, tab_name)] + sys.path
    try:
        if tab is None:
            tab = importlib.import_module(f"app")
        else:
            tab = importlib.reload(tab)
        all_tabs.append((tab_name, tab.app))

    except Exception as e:
        print(f"Error loading tab: {e}")

with gr.Blocks() as app:
    for tab_name, tab in all_tabs:
        with gr.Tab(tab_name):
            tab.render()


app.launch()
