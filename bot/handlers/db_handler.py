import sqlite3


def get_group_from_db(chat_id):
    query = "SELECT id, grp FROM USERS WHERE id=?"
    data = []
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.execute(query, [chat_id])
        for row in cursor:
            data = list(row)

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1

    finally:
        if conn:
            conn.close()
            # print(data)
            # print('SQLite Connection closed')
            return data


def get_all_id(grp):
    query = "SELECT id FROM USERS WHERE grp=?"
    data = []
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.execute(query, [grp])
        for row in cursor:
            data.append(list(row)[0])

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1

    finally:
        if conn:
            conn.close()
            # print(data)
            # print('SQLite Connection closed')
            return data


def store_in_db(chat_id, grp):
    query = '''INSERT INTO USERS (id,grp)
                VALUES (?,?)'''
    try:
        conn = sqlite3.connect('data.db')
        check_exist = get_group_from_db(chat_id)
        print(len(check_exist))
        if (check_exist != -1 and len(check_exist) == 0):
            conn.execute(query, [chat_id, grp])
            conn.commit()
            conn.close()
            return True
        else:
            return False

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return False


def update_db(chat_id, grp):
    query = '''UPDATE USERS SET grp = ? WHERE id = ?;'''
    try:
        conn = sqlite3.connect('data.db')
        check_exist = get_group_from_db(chat_id)
        # print(len(check_exist))
        if (check_exist != -1 and len(check_exist) > 0):
            conn.execute(query, [grp, chat_id])
            conn.commit()
            conn.close()
            return True
        else:
            return False

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return False
