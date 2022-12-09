from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/fancy")
def fancy_hello():
    return """
    <html>
    <body>
    <h1>Greetings!</h1>
    <p>Hello, World!<p>
    </body>
    </html>
    """

@app.route("/first_page")
def first_page():
    return render_template("first_page.html")

@app.route("/second_page")
def second_page():
    return render_template("second_page.html")

@app.route("/jinja_intro")
def jinja_intro():
    return render_template(
        "jinja_intro.html", name="Bob", template="jinja"
        )

@app.route("/expressions/")
def expressions():
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    orange_amount = 10
    apple_amout = 20
    donate_amount = 15

    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amout,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }


    return render_template(
        "expressions.html", **kwargs
        )

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data_structures/")
def data_structures():

    movies = [
        "Lion King",
        "One Piece",
        "FIFA"
    ]

    car = {
        "brand": "Tesla",
        "model": "model 3",
        "year": 2022
    }

    moons = GalileanMoons("a", "b", "c", "d")

    kwargs = {
        "movies" : movies,
        "car" : car,
        "moons" : moons,
    }

    return render_template(
        "data_structures.html", **kwargs
        )

@app.route("/conditionals_basics/")
def conditionals_basics():

    return render_template("conditionals_basics.html", company = "Apple")


@app.route("/for_loop/")
def for_loop():
    # planets = {"a": ("a", "apple"), "b": ("b", "banana")}
    planets = {"a": "apple", "b": "banana"}

    return render_template("for_loop.html", planets = planets)


@app.route("/loops_and_conditionals/")
def loops_and_conditionals():
    user_os = {"a": "Windows", "b": "MacOS", "c": "Linux"}

    return render_template("loops_and_conditionals.html", user_os = user_os)



