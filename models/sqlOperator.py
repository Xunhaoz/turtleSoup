import sqlite3


def add_message(new_message):
    conn = sqlite3.connect(r".\database.db")
    sql_command = "INSERT INTO message \
        (messages, isTrue) VALUES \
        (?, ?)"
    conn.execute(sql_command, (new_message, -1))
    conn.commit()


def get_all_message():
    conn = sqlite3.connect(r".\database.db")
    sql_command = "select * from message"
    result = []
    for i in conn.execute(sql_command).fetchall():
        result.append(i)
    return result


def delete_all_message():
    conn = sqlite3.connect(r".\database.db")
    sql_command = "delete from message"
    conn.execute(sql_command)
    conn.commit()


def delete_one_message(id):
    conn = sqlite3.connect(r".\database.db")
    sql_command = f"delete from message where id = {id}"
    conn.execute(sql_command)
    conn.commit()


def update_message(id, isTrue):
    conn = sqlite3.connect(r".\database.db")
    sql_command = "update message set isTrue = ? where id = ?"
    conn.execute(sql_command, (isTrue, id))
    conn.commit()

