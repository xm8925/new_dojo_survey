from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_dojo import Dojo


@app.route('/process', methods=['POST'])
def process():
    print(request.form)

    if Dojo.validate_dojo(request.form):
        Dojo.create(request.form)
        return redirect('/result')
    return redirect('/')
