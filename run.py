import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/livehealthy")
def livehealthy():
    return render_template("livehealthy.html", page_title="Live Healthy")


# @app.route("/careers")
# def careers():
#     return render_template("careers.html")


@app.route("/contact")
def contact():
    data = []
    with open("data/team.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("contact.html", page_title="Contact", team=data)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
