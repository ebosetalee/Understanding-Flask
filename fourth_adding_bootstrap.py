"""
Adding bootsrap and templates inheritance
https://www.youtube.com/watch?v=4nzI4RKwb5I&pbjreload=101

Flask supports inheritance of templates instead of re-writing 
the code

"""
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("extend.html")

@app.route("/test")
def test():
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)
    # Note debug restarts after every edit
