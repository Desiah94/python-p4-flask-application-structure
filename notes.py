# Initilizing the Application

#  Flask is python framework
#  First step create instance of Flask class
#  The library interacts with Flask instance using WSGI

# from flask import Flask

# app = Flask(__name__)

# Flask class constructor uses name of primary package to interprete the application
# this helps it figure out where the important files are.

# ROUTING VIEWS
# when a client sends a request to the server they are forwarded to the Flask instance
# This instance will recieve request from different URLS. To map these URLS to the function we define routes

# Routing is the URLS and the code that executes when the request comes in for that URL
# you use routes to direct request to the appropriate backend code

# the define routes we use @ap.routes decorator

# append to server/app.py
# add to server/app.py file

# @app.route('/')
# def index():
#     return '<h1>Welcome to my page!</h1>'

# @app.route() decorator is an instance method that modifies app
# creating a rule that requests from the base URL should show our index: a page with
# a header that says " Welcome to my app"
# decorator are functions that take functions as arguement
# and return them decorated with new features
# @app.route registers the index() function with the Flask application instance app

# Views functions that map to URL
# View returns the response the client sees
# index() returns HTML code, it also returns forms for cybersecurity 

#  the @app.route decorator returns data from the index()
# Registration means the view is connected to the aplications instance routes
# using the app.route decorator. When the instance recieves the URL pointing to the route, the view
# funcion is called the return value is added to the response by the instance. 

# append to server/app.py

# @app.route('/<username>')
# def user(username):
#     return f'<h1>Profile for {username}</h1>'

# Flask allows us to use different part inside the parameter for our routes.
# we interpolate thee into strings or use them to retrieve data from database
# anything included int he route passed to the app.route decorator using angle brackes <>
# will be passed to the decorator function as a parameter.
# username cann be a valid str, float, int, or path(string with slashes)

# modify user() in server/app.py

# @app.route('/<string:username>')
# def user(username):
#     return f'<h1>Profile for {username}</h1>'

# run file name to enter debugger mode. after importing debugger script
# if __name__ == '__main__':
    # app.run(port=5555, debug=True)

