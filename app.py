from flask import Flask, request, escape, url_for
from flask.templating import render_template

app=Flask(__name__)

@app.route('/')
def hello():
    name=request.args.get("name","World")
    return render_template("index.html",name=name)

@app.route('/hello/<name>')
def hello_Universe(name):
    return render_template("index.html",name=escape(name))