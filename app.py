# Team ApumpkinPI - Anton Danylenko, Derek Song, Hui Min Wu, Zane Wang
# SoftDev1 pd8
# P01 -- ArRESTed Development
# 2018-11-28

import json, urllib, os

from flask import Flask, render_template, flash, request, session

app = Flask(__name__)

choice = ""
search = ""

@app.route("/")
def generate():

    #choice = request.form["choice"]
    #search = request.form["search"]

    return render_template("homepage.html")

@app.route('/login', methods=['POST'])
def authenticate():
    '''
    checks user credentials
    logs user in and redirects to home page if username-password pair is correct
    else flashes user and redirects back to landing
    '''
    # get inputs and action type
    username = request.form['username']
    password = request.form['password']
    action = request.form['action']

    # if they're trying to log in
    if (action == 'Login'):
        # if either input is blank, redirect them back to landing
        if (username == '' or password == ''):
            flash('Invalid username or password!')
            return redirect(url_for('root_redirect'))
        # stores success value of auth fxn in dbm
        success = dbm.auth_user(username, password)

        # if login successful
        if success:
            # store username in cookies and send them home
            session['username'] = username
            return redirect(url_for('/'))
        # otherwise flash them and send them back to landing
        else:
            flash('Incorrect username or password!')
            return redirect(url_for('landing'))

    # if they want to create an account
    elif (action == 'Create Account'):
        return redirect(url_for('create_account'))

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('/create_account_action', methods=["POST"])
def create_account_action():
    username = request.form['username']
    password = request.form['password']
    password_check = request.form['password_check']

    if username == '' or password == '' or password_check == '' or ' ' in username or ' ' in password or ' ' in password_check:
        flash('Invalid username or password!')
        return redirect(url_for('create_account'))

    if password != password_check:
        flash('Passwords don\'t match!')
        return redirect(url_for('create_account'))

    success = dbm.register(username, password)

    # if account creation successful
    if success:
        # store username in cookies and send them home
        flash('Account creation successful!')
        return redirect(url_for('landing'))
    # otherwise flash them and send them back to landing
    else:
        flash('Username taken!')
        return redirect(url_for('create_account'))

@app.route('/logout')
def logout():
    '''
    if user is logged in, pops username from cookies
    regardless, redirects to landing page
    '''
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('landing'))


'''
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
