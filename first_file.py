"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! <h1>HELLO<h1>"

if __name__ == "__main__":
    app.run()
"""

# I have no idea what this does 
# figured it out - follow the link
"""
https://flask.palletsprojects.com/en/1.1.x/quickstart/
So what did that code do?

First we imported the Flask class. An instance of this class will be our WSGI application.

Next we created an instance of this class. The first argument is the name of the application’s module or package. 
If you are using a single module (as in this example), you should use __name__ because depending on if it’s started 
as application or imported as module the name will be different ('__main__' versus the actual import name). 
This is needed so that Flask knows where to look for templates, static files, and so on. 
For more information have a look at the Flask documentation.

We then used the route() decorator to tell Flask what URL should trigger our function.

The function is given a name which is also used to generate URLs for that particular function, and returns the message 
we want to display in the user’s browser.

$ export FLASK_APP=hello.py
$ flask run
* Running on http://127.0.0.1:5000/
"""

# Debug Mode:
"""
If you enable debug support the server will reload itself on code changes, 
and it will also provide you with a helpful debugger if things go wrong.

$ export FLASK_ENV=development
$ flask run

(On Windows you need to use set instead of export.)

This does the following things:
it activates the debugger
it activates the automatic reloader
it enables the debug mode on the Flask application.

You can also control debug mode separately from the environment by exporting FLASK_DEBUG=1.
"""

"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return "Hello {}".format(name)
    # return f"Hello {name}"

if __name__ == "__main__":
    app.run()
"""


# To redirect
# from flask import Flask, redirect, url_for 
# # these two allows to return a redirect from a specific function
# app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "Hello, World! <h1>HELLO<h1>"

# @app.route("/<name>")
# def user(name):
#     return "Hello {}".format(name)
#     # return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("hello_world"))

# if __name__ == "__main__":
#     app.run()


# To redirect to user, we can do this:


from flask import Flask, redirect, url_for 
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! <h1>HELLO<h1>"

@app.route("/<name>")
def user(name):
    return "Hello {}!".format(name)

@app.route("/admin")
def redirects():
    return redirect(url_for("hello_world"))

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run()