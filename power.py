from db import db


def searchpower(userinput):
    sql = "SELECT name, id FROM powers WHERE LOWER(name) LIKE LOWER(:userinput)"
    result = db.session.execute(sql, {"userinput": f"%{userinput}%"})
    return result.fetchall()


def addpower(name, desc):
    sql = "INSERT INTO powers (name, description) VALUES (:name, :description)"
    db.session.execute(sql, {"name": name, "description": desc})
    db.session.commit()


def getpower(pid):
    sql = "SELECT name, description FROM powers WHERE id = :pid"
    result = db.session.execute(sql, {"pid": pid})
    return result.fetchone()


def addplayerpower(pid, gid, uid):
    sql = "insert into powers_players(pid, uid, gid) values (:pid, :uid, :gid)"
    db.session.execute(sql, {"pid": pid, "gid": gid, "uid": uid})
    db.session.commit()


def getuserpower(uid, gid):
    sql = "select p.name, p.id from powers_players pp left join powers p on p.id = pp.pid where pp.uid = :uid and " \
          "pp.gid = :gid"
    result = db.session.execute(sql, {"gid": gid, "uid": uid})
    return result.fetchall()


def getexpandedpowers(uid, gid):
    userpower = getuserpower(uid, gid)
    return [getpower(power[1]) for power in userpower]


def rmplayerpower(pid, gid, uid):
    sql = "delete from powers_players where pid = :pid and gid = :gid and uid = :uid"
    db.session.execute(sql, {"pid": pid, "gid": gid, "uid": uid})
    db.session.commit()