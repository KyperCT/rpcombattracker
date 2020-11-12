from db import db
from werkzeug.security import check_password_hash, generate_password_hash


def getusergames(username):
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

    return [games_creator, games_user]


def login(username, password):
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if user is None:
        return False
    else:
        hash_value = user[0]
        if check_password_hash(hash_value, password):
            return [user[1], username]
        else:
            return False


def signup(username, password):
    pshash = generate_password_hash(password)
    sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
    db.session.execute(sql, {"username": username, "password": pshash})
    db.session.commit()


def addnewgame(gamename, username):
    insertgame = "INSERT INTO games (name) VALUES (:name)"
    db.session.execute(insertgame, {"name": gamename})
    db.session.commit()

    userget = "SELECT id FROM users WHERE username=:username"
    ugetresult = db.session.execute(userget, {"username": username})
    uid = ugetresult.fetchone()
    gameidget = "SELECT id FROM games WHERE name=:name"
    ggetresult = db.session.execute(gameidget, {"name": gamename})
    gid = ggetresult.fetchone()
    if uid is None:
        return False
    elif gid is None:
        return False
    else:
        insertcreator = "INSERT INTO games_users (gid, uid, creator) VALUES (:gid, :uid, TRUE)"
        db.session.execute(insertcreator, {"uid": uid[0], "gid": gid[0]})
        db.session.commit()
        return True

