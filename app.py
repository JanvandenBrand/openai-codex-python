import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        code = request.form["code"]
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=generate_prompt(code),
            temperature=0,
            max_tokens=256,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0,
            n=1,
            best_of=1,
            stop=['###']
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(code):
    return """{}""".format(
        code
    )
