# John with Amnesia

Reminder App for John!!!

# Features

* Web-based application where John can set his phone number
* Send an SMS every one hour except at night
* Resends an SMS if it fails, but retry no more than 5 times.
* The web application logs all the failed messages and tell John how many hours the application has been running.

# Documentation

Coming Soon

# Pre-Requisites

* Vonage API Account - https://www.vonage.com

# Installation

Clone this repository.

    git clone https://github.com/amanjiofficial/john-reminder.git

Create a virtualenv and activate.

    python3 -m venv env
    source env/bin/activate

Install requirement packages.

    pip install -r requirements.txt

Start the Flask application on your terminal window.

    python app.py

Application is started at http://localhost:5000/

# Maintainers

[Aman Ahuja](https://github.com/amanjiofficial)  - amanjiofficial@gmail.com
