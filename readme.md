## Feature Request App
This is a project that I created as part of a test for hiring. The app allows a user to submit feature request and also shows a list of already submitted requests.

A "feature request" is a request for a new feature that will be added onto an existing piece of
software. The fields are:

* **Title**
* **Description**
* **Client:** A selection list of clients ("Client A", "Client B", "Client C")
* **Client Priority:** A numbered priority according to the client (1...n). Client Priority numbers
do not repeat for the given client, so if a priority is set on a new feature as "1", then all
other feature requests for that client are reordered.
* **Target Date**
* **Product Area:** A selection list of product areas (use 'Policies', 'Billing', 'Claims',
'Reports')

## Tech Stack
This project was built using the following technologies:

* Server Side Scripting: Python 3.7.2
* Server Framework: Flask
* ORM: Sql-Alchemy (MySQL)
* JavaScript: JQuery
* Front-End: Bootstrap

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to have python 3.7+ running on your system.


### Installing

These instructions will give you a local repository on your machine which you can then run and use. These steps assumes you have pip installed already.

```
<!-- git clone https://github.com/emmanueljimawo/Project.git -->
pip install -r requirements.txt
python db_create_users.py
python manage.py runserver
```

## Running the tests
To run tests

```
python manage.py test

```


### Break down into end to end tests

These tests tries to cover the total functionality of this App.

The modules covered are

```
project/__init__.py
project/home/routes.py
project/models.py 	
project/users/routes.py
```

To get full information on the coverage of the test carried out

```
python manage.py cov

```

## Deployment


The app is hosted live at [Feature Request App Demo](http://52.91.234.205) using AWS EC2.
If you want a local copy, kindly follow the installation guide above.


## Authors

* **Jimawo Emmanuel** - [emmanueljimawo](https://github.com/emmanueljimawo)
