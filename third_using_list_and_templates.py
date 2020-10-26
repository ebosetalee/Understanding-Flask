from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

# To add a list of user names and loop through in the html file:
@app.route("/<name>")
def home(name):
    return render_template("list.html", content=["tim", "bisi", "chima"])


if __name__ == "__main__":
    app.run()

