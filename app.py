from flask import Flask, render_template, request
from transformers import pipeline


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def random_word_text_generation():
    if request.method == "POST":
        word = request.form.get("word")
        text_generator = pipeline('text-generation', device=-1) #, model='EleutherAI/gpt-neo-2.7B'
        content = text_generator(word, max_length=50, num_return_sequences=1)[0]["generated_text"]+"..."
        # content = text_generator(word)[0]["generated_text"]+"..."
        return render_template("index.html", content=content)

    return render_template("index.html", content=None)


if __name__ == "__main__":
    app.run(debug=True)
