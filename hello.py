# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 19:42:10 2020

@author: RUBY
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()