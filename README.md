# featureRequest

This application allows user (employee of a company) to add a new feature that will be added onto an existing piece of software. 
The information is entered after having some correspondence with the client that is requesting the feature.

### The Approach
- I created a `User` model which store a user's info and password.
- I created a `Client` model which store the type of the clients and priority. This is done so as to relate a particular client to requests 
and reorder its priority
The Client model is `related` to `Feature` Model. The feature model is used to hold the request information
(title, description, product area, target date.). This is in addition to clients information which is gotten from the Client 
model.
- A user has to register and login before gaining access to the dashboard
- A user can add and view feature requests.

### Installation

- Download or clone the app to your local machine
- Move into local directory `cd featureRequest`
- Create and acivate virtual environment. [Virtualenv](https://virtualenv.pypa.io/en/stable/) and, optionally, [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
- Run `pip install -r requirements.txt` to install the dependecies
- Run `flask db init`
- Run `flask db migrate`
- Run `flask db upgrade`
- Run `export FLASK_APP=run.py` 
- Run `flask run` and navigate to `localhost:5000` to access the app

### Deployment

The app is deployed to heroku and can be assessed on https://feature-request-heroku.herokuapp.com/


### Technologies used
The functionality of this web app depends on the following technologies.

- Flask
- Flask Login
- Jinja2
- Postgres




### Author
This is done by `Sasiliyu Adetunji`

### License & Copyright
MIT © Sasiliyu Adetunji
Licensed under the MIT License.
