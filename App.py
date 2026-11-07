
from flask import Flask, render_template, redirect, url_for

app = Flask(
    __name__,
    template_folder="Templates",
    static_folder="Static"
)

app.secret_key = "shriyafxbacktest_secret_key"


@app.route("/")
def home():
    return render_template("Index.html")


@app.route("/login")
def login():
    return render_template("Login.html")


@app.route("/register")
def register():
    return render_template("Register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html")


@app.route("/backtest")
def backtest():
    return render_template("Backtest.html")


@app.route("/analytics")
def analytics():
    return render_template("Analytics.html")


@app.route("/journal")
def journal():
    return render_template("Journal.html")


@app.route("/settings")
def settings():
    return render_template("Settings.html")


@app.route("/replay")
def replay():
    return render_template("relay.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
