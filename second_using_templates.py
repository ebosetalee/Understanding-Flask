"""
This involves using CSS or Javascript or dart

To redirect to user from the first file, we can do this:
using render_template with html templates
"""

# from flask import Flask, redirect, url_for, render_template
# app = Flask(__name__)

# # To add a user nane, we'll do:
# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", content=name)


# if __name__ == "__main__":
#     app.run()


# To write code in the html file and render it:
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

# To add a user nane, we'll do:
@app.route("/<name>")
def home(name):
    return render_template("loop.html", content=name)


if __name__ == "__main__":
    app.run()

# ["tim", "bisi", "chima"]