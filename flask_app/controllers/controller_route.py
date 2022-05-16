from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/result')
def result():
    last_dojo = Dojo.get_last()
    return render_template("result.html", last_dojo = last_dojo)



@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')