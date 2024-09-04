#This code defines your Flask routes, which will render HTML templates using Jinja
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/sample/<string:name>")
def getSampleHtml(name):
    return render_template("sample.html", name="Amore")

@main.route("/user/<username>")
def greetUser(username):
    return render_template("result.html", username=username)

@main.route('/user')
def greetOnUserBasedRequ():
    username = request.args.get("username")
    return render_template("result.html", username=username)
