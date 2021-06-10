#!/usr/bin/bash

source .venv/bin/activate
Export FLASK_ENV=development
Export FLASK_APP=app.py
flask run