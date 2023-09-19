#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/<string:operation>')
def print(operation):
    return f'<h1>Welcome to my app! {operation}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
