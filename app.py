from flask import Flask, request, render_template, send_file
from llm_prompt import generate_detailed_prompt
from image_generator import generate_image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["text"]
        style = request.form["style"]
        resolution = request.form["resolution"]

        # Prompt'u stili de dahil ederek detaylandır
        full_prompt_input = f"{user_input}. Stil: {style}, Çözünürlük: {resolution}x{resolution}."
        detailed_prompt = generate_detailed_prompt(full_prompt_input)

        image_path = generate_image(detailed_prompt, resolution=int(resolution))
        return render_template("index.html", image_path=image_path, prompt=detailed_prompt)

    return render_template("index.html")

@app.route("/download")
def download():
    return send_file("output.png", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
