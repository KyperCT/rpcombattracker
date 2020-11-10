from flask import Flask
from flask import render_template, request, session, redirect
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/games")
def games():
    username = session["username"]
    gamesget = "SELECT g.name, gu.creator FROM games g " \
               "INNER JOIN games_users gu ON g.id = gu.gid " \
               "INNER JOIN users u ON gu.uid = u.id " \
               "WHERE username = :username"
    getresult = db.session.execute(gamesget, {"username": username})
    users_games = getresult.fetchall()

    games_creator = []
    games_user = []

    for game in users_games:
        if game[1]:
            games_creator.append(game[0])
        else:
            games_user.append(game[0])

    return render_template("games.html", gmgames=games_creator, plgames=games_user)


@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user is None:
        return redirect("/games")
    else:
        hash_value = user[0]
        if check_password_hash(hash_value, password):
            session["username"] = username
            return redirect("/games")
        else:
            return redirect("/games")


@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    password = request.form["password"]
    pshash = generate_password_hash(password)
    sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
    db.session.execute(sql, {"username": username, "password": pshash})
    db.session.commit()
    session["username"] = username
    return redirect("/games")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/games/add", methods=["POST"])
def addgame():
    gamename = request.form["gamename"]
    insertgame = "INSERT INTO games (name) VALUES (:name)"
    db.session.execute(insertgame, {"name": gamename})
    db.session.commit()

    username = session["username"]
    userget = "SELECT id FROM users WHERE username=:username"
    ugetresult = db.session.execute(userget, {"username": username})
    uid = ugetresult.fetchone()
    gameidget = "SELECT id FROM games WHERE name=:name"
    ggetresult = db.session.execute(gameidget, {"name": gamename})
    gid = ggetresult.fetchone()
    if uid is None:
        return redirect("/")
    elif gid is None:
        return redirect("/")
    else:
        insertcreator = "INSERT INTO games_users (gid, uid, creator) VALUES (:gid, :uid, TRUE)"
        db.session.execute(insertcreator, {"uid": uid[0], "gid": gid[0]})
        db.session.commit()
        return redirect("/games")

