# import flask module
from flask import Flask
 
# instance of flask application
app = Flask(__name__)
 
# Home route that returns below text
# when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Bienvenue sur la formation Focker/OpenShift au CSH !</p>"