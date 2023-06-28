from flask import Flask, render_template, redirect, flash

app = Flask(__name__)


@app.route("/")
def index():
    #flash("HALOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    return '<p>fsdsdfwwwwwwwwwwwwwwwwwwwwwwwwwwwwfssdfsdf</p>'


if __name__ == "__main__":
    app.run(debug=True)