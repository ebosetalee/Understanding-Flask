"""
The two basic HTTP methods - GET, POST. They are ways of sendiing information 
to the server or clients; differences; a basic example of how to send some password
data or name date from a form to the backend of the website for processing

GET - The common way to receive or send information to a website or client.
POST - Is the secure way of receiving or semding information.
"""
# from flask import Flask, redirect, url_for, render_template


# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("extend.html")

# @app.route("/login", methods=["POST", "GET"]) # a decorator
# # methods - defining what will be allowed from these pages
# def login():
#     return render_template("login.html")

# @app.route("/<usr>")
# def user(usr):
#     return "<h1>{}</h1>".format(usr)

# if __name__ == "__main__":
#     app.run(debug=True)

"""
How to determine whether we called the GET request or the POST request:
we add request to the import; then the if statement below

In the if function, we'd like to render the login template, 
i.e if the submit button isn't clicked, we'll go on to the slash login page.
But if we have POST, we get the information "Full Name" and send us to user page
where we can display the user's name.
"""

from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("extend.html")

@app.route("/login", methods=["POST", "GET"]) # a decorator
# methods - defining what will be allowed from these pages
def login():
    if request.method == "POST":
        # a variable to store the user's name
        user = request.form["Full Name"]
        # note: request.form is a dictionary, means you can have 
        # several keys and access input values as keys. Hwever, ensure the method is POST no get.
        # to ensure it isnt't blank:
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return "<h1>{}</h1>".format(usr)

if __name__ == "__main__":
    app.run(debug=True)