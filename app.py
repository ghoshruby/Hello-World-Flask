# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 21:37:08 2020

@author: RUBY
"""


# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
