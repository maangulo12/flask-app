# -*- coding: utf-8 -*-

"""
    flask-app
    ---------------

    Run this to deploy this application
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()
