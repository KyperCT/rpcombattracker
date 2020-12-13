from db import db


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


def geteid(gameid, encid):
    sql = "select eid from games_encounters where gameid = :gid AND encounterid = :encid"
    result = db.session.execute(sql, {"gid": gameid, "encid": encid})
    eid = result.fetchone()
    return eid[0]