import logging

from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = ""
app.logger.setLevel(logging.DEBUG)


@app.route("/")
def index():
    return "hello flask"


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/hello/<name>", endpoint="hello_name")
def hello_name(name):
    return f"hello {name}"
