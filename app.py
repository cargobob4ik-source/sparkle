import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# 🌟 Мой сайт")
    gr.Markdown("Добро пожаловать!")
    
    with gr.Row():
        gr.Button("Кнопка 1")
        gr.Button("Кнопка 2")

demo.launch()
