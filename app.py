# Team ApumpkinPI - Anton Danylenko, Derek Song, Hui Min Wu, Zane Wang
# SoftDev1 pd8
# P01 -- ArRESTed Development
# 2018-11-28

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def generate():
    return render_template("homepage.html")
    
if (__name__ == "__main__"):
    app.run()
