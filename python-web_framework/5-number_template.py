#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    return "C {}".format(text).replace("_", " ")

@app.route("/python", defaults = {"text":"is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    return "Python {}".format(text).replace("_", " ")

@app.route("/number/<int:n>")
def display_number(n):
    return f"{n} is a number"

@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", n=n)




if __name__ == "__main__":
    app.run(debug=True, host= "0.0.0.0", port= 5000)
