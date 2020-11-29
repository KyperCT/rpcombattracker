from app import app
from flask import render_template, request, session, redirect, abort
from os import urandom
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
            session["csrf_token"] = urandom(16).hex()
            return redirect("/games")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if core.isusernamefree(username):
            core.signup(username, password)
            userid = core.login(username, password)
            session["userid"] = userid[0]
            session["username"] = userid[1]
            return redirect("/games")
        else:
            return render_template("error.html", error="Username is already in use")


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


@app.route("/games/search", methods=["GET"])
def gamesearch():
    searchstring = request.args["searchtext"]
    searchresults = core.searchgame(searchstring)
    return render_template("searchpage.html", searchtext=searchstring, results=searchresults)


@app.route("/games/join/<int:id>", methods=["GET", "POST"])
def joingame(id):
    if request.method == "GET":
        gamedata = core.getgame(id)
        return render_template("joinpage.html", gamename=gamedata[0], gameid=id)

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        gameid = id
        userid = session["userid"]
        try:
            core.addusertogame(gameid, userid)
        except ValueError:
            return render_template("error.html", error="You can't join a game that you're already in")
        return redirect(f"/games/{id}")


@app.route("/games/<int:id>", methods=["GET", "POST"])
def gamepage(id):
    if request.method == "GET":
        user = session["userid"]
        if core.isingame(user,id):
            gamedata = core.getgame(id)

            if session["username"] == gamedata[1]:
                iscreator = True
                session[f"iscreator{str(id)}"] = True
            else:
                iscreator = False
                session[f"iscreator{str(id)}"] = False

            encounters = core.getencounters(id)

            return render_template("gamepage.html", gamename=gamedata[0], creator=gamedata[1], Players=gamedata[2],
                                    iscreator=iscreator, gameid=id, Encounters=encounters)
        else:
            return render_template("error.html", error="You are not authorized to view this page")

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        charname = request.form["CharName"]
        core.namecharacter(id, session["userid"], charname)
        return redirect(f"/games/{id}", code=303)


@app.route("/games/<int:id>/addenc", methods=["POST"])
def addencounter(id):
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    gameid = id
    core.newencounter(gameid)
    return redirect(f"/games/{id}")


@app.route("/games/<int:gid>/enc/<int:encid>", methods=["POST", "GET"])
def encounter(gid,encid):
    if request.method == "GET":
        try:
            phase = session[f"encphase{str(gid)}{str(encid)}{session['userid']}"]
        except KeyError:
            return render_template("encounter.html", gid=gid, encid=encid, phase0=True, phase1=False,
                                   iscreator=session[f"iscreator{str(gid)}"])
        if phase == 1:
            initdata = core.getinitdata(gid, encid)
            return render_template("encounter.html", gid=gid, encid=encid, phase0=False, phase1=True,
                                   iscreator=session[f"iscreator{str(gid)}"], initdata=initdata)

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        if request.form["post_type"] == "0":
            monsternames = {x[-1]: request.form[x] for x in request.form if x[0][0] == "M"}
            initiatives = {x[-1]: request.form[x] for x in request.form if x[0][0] == "I"}
            core.addmonstersinit(monsternames, initiatives, gid, encid)

            session[f"encphase{str(gid)}{str(encid)}{session['userid']}"] = 1
            return redirect(f"/games/{gid}/enc/{encid}", code=303)

        if request.form["post_type"] == "1":
            initnum = request.form["Initnum"]
            core.addinitiative(gid, encid, session["userid"], initnum)

            session[f"encphase{str(gid)}{str(encid)}{session['userid']}"] = 1
            return redirect(f"/games/{gid}/enc/{encid}", code=303)

