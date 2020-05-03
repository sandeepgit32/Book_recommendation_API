# REST API for Book Recommendation

## Installation

Use `virtualenv` to isolate packages.

Use pip to install the packages in the requirements file:
```
$ pip install -r requirements.txt
```

## Initializing the db

To run the app, the database must be initialized:
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```

## Running the app

Just run the script using the following command:
```
$ python manage.py runserver
```

## Error debugging

For Python 3.7 and Ubuntu in particular, install ```libpython-dev```
```
sudo apt install libpython3.7-dev
```
I think at some point names were changed from pythonm.n-dev to this.

Downgrading to Werkzeug==0.16.1