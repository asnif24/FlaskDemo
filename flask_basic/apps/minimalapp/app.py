import logging

from email_validator import EmailNotValidError, validate_email
from flask import (
    Flask,
    current_app,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
)

app = Flask(__name__)

app.config["SECRET_KEY"] = "ftfhgbvcrd65456476rfggchgc"
app.logger.setLevel(logging.DEBUG)

ctx = app.app_context()
ctx.push()


@app.route("/")
def index():
    return "hello flask"


@app.route("/hello")
def hello():
    return "hello world"


@app.route("/hello/<name>", endpoint="hello_name")
def hello_name(name):
    print(current_app.name)
    g.connection = "connection"
    print(g.connection)
    return render_template("index.html", name=name)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        description = request.form.get("description")

        is_valid = True

        if not username:
            flash("必填 username")
            is_valid = False

        if not email:
            flash("必填 email")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("請輸入正確email格式")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))

        if not description:
            flash("必填 description")
            is_valid = False

        flash("諮詢內容已傳送")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")
