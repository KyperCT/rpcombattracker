from sqlalchemy import exc

from encounter import geteid
from db import db


def addinitiative(gameid: int, encid: int, uid: int, initnum: int):
    eid = geteid(gameid, encid)
    try:
        insertsql = "insert into initiative (eid, uid, initnum) values (:eid, :uid, :initnum)"
        db.session.execute(insertsql, {"eid": eid, "uid": uid, "initnum": initnum})
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        updatesql = "update initiative set initnum = :initnum where eid = :eid AND uid = :uid"
        db.session.execute(updatesql, {"eid": eid, "uid": uid, "initnum": initnum})
        db.session.commit()


def addmonstersinit(monsterlist, initiativelist, gameid, encid):
    eid = geteid(gameid, encid)
    fulllist = [(monsterlist[x], initiativelist[x]) for x in monsterlist]
    sql = "insert into monsters_initiative (eid, monstername, initiative) values (:eid, :mname, :initnum)"
    for monster in fulllist:
        db.session.execute(sql, {"eid": eid, "mname": monster[0], "initnum": monster[1]})
    db.session.commit()


def getinitdata(gid, encid):
    sql = "select initnum, charname from initiative i " \
          "inner join games_encounters ge on i.eid = ge.eid " \
          "inner join games_users gu on (ge.gameid = gu.gid AND i.uid = gu.uid) " \
          "where gu.gid = :gid and ge.encounterid = :encid"
    result = db.session.execute(sql, {"gid": gid, "encid": encid})
    data = result.fetchall()
    monstersql = "select i.initiative, i.monstername, i.id from monsters_initiative i " \
                 "inner join games_encounters ge on i.eid = ge.eid " \
                 "where ge.gameid = :gid and ge.encounterid = :encid"
    monsterresult = db.session.execute(monstersql, {"gid": gid, "encid": encid})
    mresult = []
    for row in monsterresult:
        mresult.append(list(row))
    for row in mresult:
        row.append(True)
    data.extend(mresult)

    return list(sorted(data, key=lambda x: x[0], reverse=True))


def rmmonster(mid):
    sql = "delete from monsters_initiative where id = :mid"
    db.session.execute(sql, {"mid": mid})
    db.session.commit()