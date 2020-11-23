"""
Message flashing is showing some kind of information from a previous page on
the next page when something happens on GUI(graphical user interface).
For example, login redirects to another page which says login successfully etc

Flashes message for the user to know what has been done, like a feedback.

import flash
Then use fash function to diaplay or POST the messages that need to be flashed.

edit login.html in the block content

I realised this is frontend.... Paused the tutorial here
link: https://www.youtube.com/watch?v=qbnqNWXf_tU follow the course(if interested).
"""

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "star"
app.permanent_session_lifetime = timedelta(hours=12)

@app.route("/")
def home():
    return render_template("extend.html")

@app.route("/login", methods=["POST", "GET"]) 
def login():
    if request.method == "POST":
        session.permanent = True 
        user = request.form["Full Name"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user", usr=user))
    elif "user" in session:
        flash("Already Logged In!")
        return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user) # changed this to render
        # The user template instead of name. 
    flash("You are not logged in!")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # we'll need to flash in Logout so the they know they logged out
    # when directed to the login page through the pop.
    session.pop("user", None)
    flash("You have been logged out!", "info") # the next parameter is 
    # the category which is optional, info and error are the built-in 
    # to show icons or data beside it. This is it for flash, the need is 
    # to display the messages in different pages.
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)