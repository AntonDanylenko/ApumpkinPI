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
#### Obtaining Keys
##### New York Times Movies Review
Provides movie reviews and ratings.

Obtain an API key [here](https://developer.nytimes.com/signup).

##### OMDB
Provides thorough information about movies.

Fill out the form [here](http://www.omdbapi.com/apikey.aspx?__EVENTTARGET=freeAcct&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE=%2FwEPDwUKLTIwNDY4MTIzNQ9kFgYCAQ9kFgICBw8WAh4HVmlzaWJsZWhkAgIPFgIfAGhkAgMPFgIfAGhkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYDBQtwYXRyZW9uQWNjdAUIZnJlZUFjY3QFCGZyZWVBY2N0x0euvR%2FzVv1jLU3mGetH4R3kWtYKWACCaYcfoP1IY8g%3D&__VIEWSTATEGENERATOR=5E550F58&__EVENTVALIDATION=%2FwEdAAU5GG7XylwYou%2BzznFv7FbZmSzhXfnlWWVdWIamVouVTzfZJuQDpLVS6HZFWq5fYpioiDjxFjSdCQfbG0SWduXFd8BcWGH1ot0k0SO7CfuulN6vYN8IikxxqwtGWTciOwQ4e4xie4N992dlfbpyqd1D&at=freeAcct&Email=) to get an API key.

##### New York Public Library 
Provides thorough information about books.

Get API key by signing up [here](http://api.repo.nypl.org/).

#### Inputting Keys
Once you've obtained all the keys, replace the keys in ```keys.txt``` with your own, in the order in which the APIs are listed above. One key should occupy each line
