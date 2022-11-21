import sqlite3


def get_group_from_db(chat_id):
    query = "SELECT id, grp FROM USERS WHERE id=?"
    data = []
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.execute(query, [chat_id])
        for row in cursor:
            data = list(row)
        conn.close()
        return data

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1


def create_table():
    query = '''CREATE TABLE USERS (
	                id INT PRIMARY KEY NOT NULL,
	                grp TEXT NOT NULL
                    );'''
    drop_query = "DROP TABLE IF EXISTS USERS;"
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute(drop_query)
        conn.execute(query)
        conn.commit()
        conn.close()
        return True

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1


def get_all_id(grp):
    query = "SELECT id FROM USERS WHERE grp=?"
    data = []
    try:
        conn = sqlite3.connect('data.db')
        grp = grp.upper()
        cursor = conn.execute(query, [grp])
        for row in cursor:
            data.append(list(row)[0])
        conn.close()
        return data

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1


def get_list_of_id(grp_list):
    grp_list = list(map(str, grp_list))
    qst = '?,'*len(grp_list)
    query = f"SELECT id FROM USERS WHERE grp in ({qst[:-1]})"
    id_list = []
    try:
        conn = sqlite3.connect('data.db')
        cursor = conn.execute(query, [*grp_list])
        for row in cursor:
            id_list.append(list(row)[0])
        conn.close()
        return id_list

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1


def store_in_db(chat_id, grp):
    query = '''INSERT INTO USERS (id,grp)
                VALUES (?,?)'''
    try:
        conn = sqlite3.connect('data.db')
        check_exist = get_group_from_db(chat_id)
        # print(len(check_exist))
        if (check_exist != -1 and len(check_exist) == 0):
            conn.execute(query, [chat_id, grp])
            conn.commit()
            conn.close()
            return True
        else:
            return False

    except sqlite3.Error as error:
        # print('Error occurred - ', error)
        return -1


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
        return -1
