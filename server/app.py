#!/usr/bin/env python3
import os

from flask import Flask, request, current_app, g, make_response, redirect, url_for

app = Flask(__name__)


# # 1. view function that uses a request obj
# @app.route('/')
# def index():
#     host = request.headers.get("Host")
#     return f'<h1>The host for this page is {host}</h1>'


# 2. Flask application context
@app.route('/')
def index():
    host = request.headers.get("Host")
    appname = current_app.name

    # 4-1. create a body_String
    response_body = f'''<h1>The host for this page is {host}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.path}</h3>'''
    
    # 4-2. send a status code, as a 2nd return value after response body
    status_code = 202

    # 4-3: a headers dict
    headers = {}

    # 4-4: return response using make_response
    return make_response(response_body, status_code, headers)



# 3. set up a hook for views to know where the app files are located
@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())


# 5. redirect to homepage index view
# @app.route('/user/<string:username>')
# def user(username):
    # if username == "flask":
    #     return redirect(url_for('index'))
    
# 6. using url_for
@app.route('/user')
def user():
    url = url_for('index')
    return f"<a href={ url }>Homepage</a>"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
