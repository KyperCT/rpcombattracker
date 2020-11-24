from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import exc

def getusergames(username):
    gamesget = "SELECT g.name, gu.creator, g.id FROM games g " \
               "INNER JOIN games_users gu ON g.id = gu.gid " \
               "INNER JOIN users u ON gu.uid = u.id " \
               "WHERE username = :username"
    getresult = db.session.execute(gamesget, {"username": username})
    users_games = getresult.fetchall()

    games_creator = []
    games_user = []

    for game in users_games:
        if game[1]:
            games_creator.append((game[0], game[2]))
        else:
            games_user.append((game[0], game[2]))

    return [games_creator, games_user]


def isusernamefree(username):
    usersql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(usersql, {"username": username})
    user = result.fetchone()
    if user is None:
        return True
    else:
        return False


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
    gameidget = "SELECT id FROM games WHERE name=:name ORDER BY id DESC LIMIT 1"
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


def isingame(user, game):
    sql = "SELECT u.id FROM users u " \
          "INNER JOIN games_users gu ON u.id = gu.uid " \
          "WHERE u.id=:uid AND (gu.gid=:gid OR u.admin = TRUE)"
    result = db.session.execute(sql, {"gid":game,"uid":user})

    if result.fetchone() is None:
        return False
    else:
        return True


def getgame(id):
    sql = "select g.name, u.username, gu.creator from games g " \
          "inner join games_users gu on g.id = gu.gid " \
          "inner join users u on gu.uid = u.id " \
          "where g.id = :id "
    result = db.session.execute(sql, {"id": id})
    data = result.fetchall()
    output = []
    users = []
    for row in data:
        if row[2]:
            output.append(row[0])
            output.append(row[1])
        else:
            users.append(row[1])
    output.append(users)
    return output

def searchgame(userinput):
    sql = "SELECT name, id FROM games WHERE name LIKE :userinput"
    result = db.session.execute(sql, {"userinput": f"%{userinput}%"})
    return result.fetchall()


def addusertogame(gameid: int,userid: int):
    sql = "INSERT INTO games_users (gid, uid) VALUES (:gid, :uid)"
    try:
        db.session.execute(sql, {"gid": gameid, "uid": userid})
        db.session.commit()
    except exc.IntegrityError:
        raise ValueError


def newencounter(gameid):
    fetchencounternum = "SELECT encounterid FROM games_encounters " \
                        "WHERE gameid = :gameid ORDER BY encounterid DESC LIMIT 1"
    latestenc = db.session.execute(fetchencounternum, {"gameid": gameid})
    encounter = latestenc.fetchone()
    if encounter is None:
        encounter = 0
    else:
        encounter = encounter[0]
    addencounter = "INSERT INTO games_encounters (encounterid, gameid) VALUES (:encid,:gid)"
    db.session.execute(addencounter, {"encid": encounter+1, "gid": gameid})
    db.session.commit()


def getencounters(gameid: int):
    sql = "SELECT encounterid FROM games_encounters WHERE gameid = :gameid"
    result = db.session.execute(sql, {"gameid": gameid})
    encids = map(lambda item: item[0], result.fetchall())
    return list(encids)
