from app import app
from flask import render_template, request, session, redirect
import core

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/games")
def games():
    usergames = core.getusergames(session["username"])
    return render_template("games.html", gmgames=usergames[0], plgames=usergames[1])


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        getlogin = core.login(request.form["username"], request.form["password"])
        if getlogin is False:
            return redirect("/")
        else:
            session["userid"] = getlogin[0]
            session["username"] = getlogin[1]
            return redirect("/games")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        core.signup(username, password)
        userid = core.login(username, password)
        session["userid"] = userid[0]
        session["username"] = userid[1]
        return redirect("/games")


@app.route("/logout")
def logout():
    del session["username"]
    del session["userid"]
    return redirect("/")


@app.route("/games/add", methods=["POST"])
def addgame():
    newgame = core.addnewgame(request.form["gamename"], session["username"])
    if newgame:
        return redirect("/games")
    else:
        return redirect("/")


@app.route("/games/<int:id>")
def gamepage(id):
    user = session["userid"]
    if core.isingame(user,id):
        gamedata = core.getgame(id)
        return render_template("gamepage.html", gamename=gamedata[0], creator=gamedata[1], Players=gamedata[2])
    else:
        return render_template("error.html", error="You are not authorized to view this page")
