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

#_choice = ""
#search = ""

def setUser(userName):
    global user
    user = userName

@app.route('/', methods=['POST', 'GET'])
def home():
    if user in session:
        data = pumpkin.DB_Manager(DB_FILE)
        return render_template('hometemp.html', user_name = user, loggedin = "True")


    return render_template("hometemp.html")

@app.route('/auth', methods=['POST'])
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
        return redirect(url_for("home"))

@app.route('/create_account_action', methods=["POST"])
def create_account_action():
    data = pumpkin.DB_Manager(DB_FILE)
    username, password, password2 = request.form["username_reg"], request.form['password_reg'], request.form['password_check']
    if len(username.strip()) != 0 and not data.findUser(username):
        if len(password.strip()) != 0:
            # add the account to DB
            if password != password2:
                flash('Passwords must match')
            else:
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

@app.route('/return')
def ret():
    return redirect(url_for('home'))

@app.route("/search", methods = ["GET", "POST"])
def search():

    search = request.args["search"]
    if (search == ""):
        flash("Please input something in search!")
    else:
        _search = ""

        for i in search: # in case there are multiple word titles
            if (i == " "):
                _search = _search + "+"
            else:
                _search = _search + i

        okey = "b7503b8d"
        omdb = "http://www.omdbapi.com/?apikey=" + okey + "&"

        nytkey = "7e297703ad9e4b9595f9d7b9bff79582"
        nyt = "http://api.nytimes.com/svc/movies/v2/reviews/search.json?query="

        nyplkey = "4w5dn9nta332kd9r"
        nypl = "http://api.repo.nypl.org/api/v1/items/search?q="

        mdata = {}

        #if (_choice == "name"):
        mtitle = "t=" + _search # gets the movie title that was searched and formats it for the api to work
        omdburl = omdb + mtitle
        x = urllib.request.urlopen(omdburl).read()
        mdata = json.loads(x)
        print("MDATA--------------------")
        print(mdata)

        nyturl = nyt + _search + "&api-key=" + nytkey
        y = urllib.request.urlopen(nyturl).read()
        critique = json.loads(y)
        print("CRITIQUE-----------------")
        print(critique)

        args = {}
        args['title'] = mdata['Title']
        args['year'] = mdata['Year']
        args['actors'] = mdata['Actors']
        args['rating'] = mdata['Rated']
        args['genre'] = mdata['Genre']
        args['desc'] = mdata['Plot']
        args['mposter'] = mdata['Poster']
        args['critique'] = critique['results'][0]['link']['suggested_link_text']
        args['link'] = critique['results'][0]['link']['url']
        print(args)
        if user in session:
            sesh = "True"
        else:
            sesh = ""
        return render_template('movie.html', **args, loggedIn = sesh)
    return redirect(url_for("home"))

@app.route("/favorites")
def favList():
    data = pumpkin.DB_Manager(DB_FILE)

    if isInDB(data, "favorites"):
        printList = {}
        favList = data.table(data, "favorites")
        for x in favList:
            if user == x:
                printList[x] = favList[x]
                return render_template("favList.html", table=printList)
            else:
                flash("No favorites found!")
                return redirect(url_for("home"))

@app.route("/addfave")
def addFave():
    #opens the db, checks if table exists
    data = pumpkin.DB_Manager(DB_FILE)
    data.tableCreator("favorites", "user", "movie")
    #add title of movie as a tuple to the favorites table
    tup = (title)
    data.insertRow(data, "favorites", tup)
    data.save(data)
    return redirect(url_for("home"))

if (__name__ == "__main__"):
    app.debug = True
    app.run()
