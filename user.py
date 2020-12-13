from werkzeug.security import check_password_hash, generate_password_hash

from db import db


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