# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:37:08 2020

@author: RUBY
"""


from flask import Flask,request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    
    name = request.args.get("name", None)

@app.route('/')
def index():
    return "<h1>Hello World !!</h1>"

if __name__ == '__main__':
    
    app.run()
