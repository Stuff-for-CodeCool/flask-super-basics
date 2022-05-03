from flask import Flask, render_template, request
import data_manager

app = Flask(__name__)


@app.get("/ceva/altceva/<x>")
def treburi(x):
    return f"ics este {x}"


@app.get("/")
def index():
    # primes = {
    #     "ala": "bala",
    #     "portocala": "fruct citric"
    # }
    primes = [1, 2, 3, 4, 5, 6, 7]

    return render_template("index2.html", chestii=primes)


@app.get("/form")
def show_form():
    return render_template("form.html")


@app.post("/form")
def process_form():
    name = request.form.get("nume")
    return render_template(
        "response.html",
        gigel=data_manager.greet(name),
    )


if __name__ == "__main__":
    app.run(debug=True)
