#!/usr/bin/bash

source .venv/Scripts/activate
Export FLASK_ENV=development
Export FLASK_APP=app.py
flask run