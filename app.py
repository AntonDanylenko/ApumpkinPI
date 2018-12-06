# Team ApumpkinPI - Anton Danylenko, Derek Song, Hui Min Wu, Zane Wang
# SoftDev1 pd8
# P01 -- ArRESTed Development
# 2018-11-28

import json, urllib, os

from flask import Flask, render_template, flash, request, session, redirect, url_for

from utils import db as pumpkin

DB_FILE = "data/ApumpkinPI.db"
app = Flask(__name__)
user = None
currStory = None
app.secret_key = os.urandom(32)

def setUser(userName):
    global user
    user = userName

@app.route('/')
def home():
    if user in session:
        data = pumpkin.DB_Manager(DB_FILE)
        return render_template('user.html', user_name = user)
    return render_template("hometemp.html")

'''@app.route('/login_menu')
def login():
    return redirect(url_for("auth"))

@app.route('/register_menu')
def register():
    return redirect(url_for("auth"))'''

@app.route('/auth', methods=['GET'])
def auth():
    # instantiates DB_Manager with path to DB_FILE
    data = pumpkin.DB_Manager(DB_FILE)
    # LOGGING IN
    if request.form["action"] == "Login":
        username, password = request.form["username_login"], request.form['password_login']
        if username != "" and password != "" and data.verifyUser(username, password ) :
            session[username] = password
            setUser(username)
            data.save()
            return redirect(url_for('home'))
        # user was found in DB but password did not match
        elif data.findUser(username):
            flash('Incorrect password!')
        # user not found in DB at all
        else:
            flash('Incorrect username!')
        data.save()
        return render_template("homelogin.html")
    # REGISTERING
    elif request.form["action"] == "Create Account":
        username, password = request.form["username_reg"], request.form['password_reg']
        if len(username.strip()) != 0 and not data.findUser(username):
            if len(password.strip()) != 0:
                # add the account to DB
                data.registerUser(username, password)
                data.save()
                return redirect(url_for('home'))
            else:
                flash('Password needs to have stuff in it')
        elif len(username) == 0:
            flash("Username needs to have stuff in it")
        else:
            flash("Username already taken!")
        # TRY TO REGISTER AGAIN
        return render_template("hometemp.html")

@app.route('/logout')
def logout():
    session.pop(user, None)
    setUser(None)
    return redirect(url_for('home'))

'''
choice = ""
search = ""

@app.route("/")
def generate():

    #choice = request.form["choice"]
    #search = request.form["search"]

    return render_template("hometemp.html")

@app.route("/login_menu")
def login_menu():
    return render_template("homelogin.html")

@app.route("/register_menu")
def register_menu():
    return render_template("homeregister.html")

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

    mdata = {}

    if (choice == "name"):
        mtitle = "t=" + search # gets the movie title that was searched and formats it for the api to work
        omdburl = omdb + mtitle
        x = urllib.request.urlopen(omdburl).read()
        mdata = json.loads(x)
        print(mdata)

    #if (choice == "date"):
    #    myear = "y=" + request.form['search'] # gets the year that was searched and formats it
    #    omdburl = omdb + myear
    #    x = urllib.request.urlopen(omdburl).read()
    #    mdata = json.loads(x)

    #if (choice == "cast"):
    #if (choice == "genre"):

    args = {}
    args['title'] = mdata['Title']
    args['year'] = mdata['Year']
    args['actors'] = mdata['Actors']
    args['rating'] = mdata['Ratings']

    return render_template('movie.html', **args)

if (__name__ == "__main__"):
    app.debug = True
    app.run()
