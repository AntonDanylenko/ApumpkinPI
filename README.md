# ApumpkinPI

### Team Roster
PM: Anton Danylenko
Hui Min Wu
Derek Song
Zane Wang

### Project Description
EncycloCinema is a site where you can input a movie name, date, or genre and receive information about that movie such as the cast and reviews. If available, the books related to the movie you searched are also shown. If you make an account on the site, you can save movies you like and be recommended similar movies.

### How To Run
1. Clone the ApumpkinPI repo.
2. Enter your venv.

If you do not have a virtual environment:
  * Install virtualenv with ```$ pip install virtualenv```
  * Make your venv with ```$ python3 -m venv venv_name```
  * Activate venv with ```$ . /venv_name/bin/activate```
  * When done, deactivate venv with ```$ deactivate```
3. Install all necessary pluginswith:
```(venv)$pip install -r <path-to-file>requirements.txt```
4. Run ```$ python app.py```
5. Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) on your preffered browser to open the site.


### Api Information
#### New York Times Movies Review
Provides movie reviews and ratings.

Obtain an API key [here](https://developer.nytimes.com/signup).

#### OMDB
Provides thorough information about movies.

Currently there is an issue with getting API key, will be updated soon.

#### New York Public Library 
Provides thorough information about books.

Get API key by signing up [here](http://api.repo.nypl.org/).
