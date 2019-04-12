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

<!-- The app is hosted live at [Feature Request App Demo](http://featuredemoapp.us-west-1.elasticbeanstalk.com/) thanks to AWS Elastic Beanstalk and RDS, but if you want a local copy, continue reading.

These instructions will give you a local repository on your machine which you can then run and use. These steps assumes you have pip installed already. -->

```
<!-- git clone https://github.com/mariesta/FeatureRequestApp.git -->
pip install -r requirements.txt
python create_db.py
python run.py
```

# Project Title

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

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
