"""
In the Login Page, we redirect to a page that shows their name, but
everytime we want to see the user's name, we need to login again and again.
what if we want to direct to another page and that page needs the user's name too. 
Thus, we'll have to set up a way to pass the user's name by using the parameter

To do this without redirecting to the /<name> we use sessions.
Sessions are temporary, stored on the web server, for quick access to information
between all the different pages of the website - i.e only available based on the user.

import sessions
"""

from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
# Everything is stored in a server so we need to define the encrypt and decrypt key.
app.secret_key = "star" # can type anythin in the string for encrypting.
# we can set how long we want the information in session to be stored for by 
# using permanent sessions; using datetime module
app.permanent_session_lifetime = timedelta(hours=12)
# Note: do not store permanent data in a session

@app.route("/")
def home():
    return render_template("extend.html")

@app.route("/login", methods=["POST", "GET"]) 
def login():
    if request.method == "POST":
        session.permanent = True #This definition means it'll last as long as default
        user = request.form["Full Name"]
        session["user"] = user
        # session stores data as a dictionary
        return redirect(url_for("user", usr=user))
    elif "user" in session:
        return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user")
def user():
    # check if there's any data in that session before getting it
    if "user" in session:
        user = session["user"]
        return "<h1>{}</h1>".format(user)
    return redirect(url_for("login"))

# Create a login page, and manually clear a session
@app.route("/logout")
def logout():
    session.pop("user", None) # to remove session data for user
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)