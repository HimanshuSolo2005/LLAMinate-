import gradio as gr
import subprocess

def convert_python_to_cpp(python_code: str) -> str:
    prompt = f"""You are a code assistant that converts Python code to high-performance C++.
Only respond with the converted C++ code, without any explanation or markdown.

Here is the Python code:
{python_code}
"""
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        cpp_code = result.stdout.decode("utf-8")

        with open("main_converted.cpp", "w") as f:
            f.write(cpp_code)

        return cpp_code
    except subprocess.TimeoutExpired:
        return "Error: LLaMA 3 response timed out."
    except Exception as e:
        return f"Exception: {str(e)}"


with gr.Blocks(theme=gr.themes.Base()) as demo:

    gr.Markdown("# 🧑‍💻 Python ➜ C++ Code Converter")
    gr.Markdown("🚀 Powered by LLaMA 3 (via Ollama)")

    theme_choice = gr.Dropdown(
        choices=["Light", "Dark"],
        value="Light",
        label="Choose Theme"
    )

    with gr.Row():
        with gr.Column():
            code_input = gr.Textbox(
                lines=20,
                placeholder="Paste Python code here...",
                label="Python Code",
                elem_id="python_input"
            )
            submit_btn = gr.Button("⚙️ Convert")

        with gr.Column():
            cpp_output = gr.Textbox(
                lines=20,
                label="Converted C++ Code",
                interactive=True,
                elem_id="cpp_output"
            )

            copy_button = gr.Button("📋 Copy Code")

    submit_btn.click(fn=convert_python_to_cpp, inputs=code_input, outputs=cpp_output)

    copy_button.click(
        None,
        None,
        None,
        js="""
        () => {
            const code = document.querySelector('#cpp_output textarea').value;
            navigator.clipboard.writeText(code);
            alert('✅ Code copied!!');
        }
        """
    )

    def update_theme(selected_theme):
        return gr.themes.Base() if selected_theme == "Light" else gr.themes.Soft()

    theme_choice.change(fn=update_theme, inputs=theme_choice, outputs=[], queue=False)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)

