# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:37:08 2020

@author: RUBY
"""


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    



# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Hello World !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
