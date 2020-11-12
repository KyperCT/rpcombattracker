from app import app
from flask import render_template, request, session, redirect
import usermanage as usrman


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/games")
def games():
    usergames = usrman.getusergames(session["username"])
    return render_template("games.html", gmgames=usergames[0], plgames=usergames[1])


@app.route("/login",methods=["POST"])
def login():
    getlogin = usrman.login(request.form["username"], request.form["password"])
    if getlogin is False:
        return redirect("/")
    else:
        session["username"] = getlogin
        redirect("/games")


@app.route("/signup", methods=["POST"])
def signup():
    sendsignup = usrman.signup(request.form["username"], request.form["password"])
    session["username"] = sendsignup
    return redirect("/games")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/games/add", methods=["POST"])
def addgame():
    newgame = usrman.addnewgame(request.form["gamename"],session["username"])
    if newgame:
        return redirect("/games")
    else:
        return redirect("/")

