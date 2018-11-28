# Team ApumpkinPI - Anton Danylenko, Derek Song, Hui Min Wu, Zane Wang
# SoftDev1 pd8
# P01 -- ArRESTed Development
# 2018-11-28

from flask import Flask, render_template, flash

app = Flask(__name__)

@app.route("/")
def generate():
    return render_template("homepage.html")
'''
@app.route("/login")
    render_template("login.html")

@app.route("/register")
    render_template("register.html")

@app.route("/movies")
    render_template("<>.html")

@app.route("/info")
    render_template("<>.html")
'''

if (__name__ == "__main__"):
    app.run()
