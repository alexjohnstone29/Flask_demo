from flask import Flask

app = Flask(__name__)


@app.route("/c")
@app.route("/c/<celsius>")
def celsius_to_fahrenheit(celsius=0):
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return "{}".format(fahrenheit)


@app.route("/f")
@app.route("/f/<fahrenheit>")
def fahrenheit_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - 32) * 5 / 9
    return "{}".format(celsius)
