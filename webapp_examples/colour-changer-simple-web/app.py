from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colour = f"{r}, {g}, {b}"
    else:
        colour = "255, 255, 255"
    return render_template("index.html", colour=colour)


if __name__ == "__main__":
    app.run(debug=True)
