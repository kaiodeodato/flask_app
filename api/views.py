from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    name = "tim"
    return render_template("index.html", name=name)

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'john', 'coolness': 10})


@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))

@views.route("/users/<username>")
def users(username):
    if not username:
        username = 'other'
    return render_template("profile.html", name= username)