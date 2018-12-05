# Team ApumpkinPI - Anton Danylenko, Derek Song, Hui Min Wu, Zane Wang
# SoftDev1 pd8
# P01 -- ArRESTed Development
# 2018-11-28

import json, urllib

from flask import Flask, render_template, flash, request

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

@app.route("/search", methods = ["POST", "GET"])
def search():
    okey = "b7503b8d"
    omdb = "http://www.omdbapi.com/?apikey=" + okey + "&"

    nytkey = "7e297703ad9e4b9595f9d7b9bff79582"
    nyt = ""

    if (request.select['choice'] == "name"):
        mtitle = "t=" + request.form['search'] # gets the movie title that was searched and formats it for the api to work
        omdburl = omdb + mtitle
        x = urllib.request.urlopen(omdburl).read()
        mdata = json.loads(x)
        #print(mdata)
    if (request.select['choice'] == "date"):
        myear = "y=" + request.form['search'] # gets the year that was searched and formats it
        omdburl = omdb + myear
        x = urllib.request.urlopen(omdburl).read()
        mdata = jason.loads(x)
    #if (request.select['choice'])
        args = {}
        args['title'] = mdata['Title']
        args['year'] = mdata['Year']
        args['actors'] = mdata['Actors']
        args['rating'] = mdata['Ratings']

    return render_template('movie.html', **args)

if (__name__ == "__main__"):
    app.debug = True
    app.run()
