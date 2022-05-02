import socket
import sqlite3
from datetime import datetime


def get_timestamp():
    # Converting datetime object to string
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%Y-%m-%d (%H:%M:%S)")
    # 2022-04-27 17:35:28.010846
    # ct = datetime.now()
    print('Current Timestamp : ', timestampStr)
    return timestampStr
    # return ct


def get_ipaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ipaddr = ''
    try:
        # doesn't even have to be reachable
        ipaddr = socket.gethostbyname(socket.gethostname())
    except Exception:
        print("Cloud not get the IP address...")
    finally:
        s.close()
    return ipaddr


def create_user_in_word():
    try:
        # Connecting to sqlite
        # connection object
        connection_obj = sqlite3.connect('log_data.db')

        # cursor object
        cursor_obj = connection_obj.cursor()

        # Drop the user_in_word table if already exists.
        cursor_obj.execute("DROP TABLE IF EXISTS user_in_word")

        # Creating table
        create_user_in_word_query = '''CREATE TABLE IF NOT EXISTS user_in_word(
            word_id INTEGER PRIMARY KEY,
            w1 CHAR(5),
            w2 CHAR(5),
            w3 CHAR(5),
            w4 CHAR(5),
            w5 CHAR(5),
            w6 CHAR(5)
            );
        '''
        cursor_obj.execute(create_user_in_word_query)
        connection_obj.commit()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (connection_obj):
            connection_obj.close()
            print("sqlite connection is closed")


def create_win_stats():
    try:
        # Connecting to sqlite
        # connection object
        connection_obj = sqlite3.connect('log_data.db')

        # cursor object
        cursor_obj = connection_obj.cursor()

        # Drop the user_win_stats table if already exists.
        cursor_obj.execute("DROP TABLE IF EXISTS user_win_stats")

        # Creating table
        create_win_stat_query = '''CREATE TABLE IF NOT EXISTS user_win_stats(
            win_id INTEGER PRIMARY KEY,
            win INTEGER 
            );
        '''
        cursor_obj.execute(create_win_stat_query)
        connection_obj.commit()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (connection_obj):
            connection_obj.close()
            print("sqlite connection is closed")


def create_log_table():
    try:
        # Connecting to sqlite
        # connection object
        connection_obj = sqlite3.connect('log_data.db')

        # cursor object
        cursor_obj = connection_obj.cursor()

        # Drop the log table if already exists.
        cursor_obj.execute("DROP TABLE IF EXISTS log")

        # Creating table
        create_log_query = '''CREATE TABLE IF NOT EXISTS log(
            g_id INTEGER PRIMARY KEY,
            dt CHAR(21),
            ip CHAR(15),
            selected_word CHAR(5),
            win_id INTEGER NOT NULL,
            word_id INTEGER NOT NULL
            );
        '''
        cursor_obj.execute(create_log_query)
        connection_obj.commit()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (connection_obj):
            connection_obj.close()
            print("sqlite connection is closed")


# insert prev_tried_words into user_in_word
def insert_user_in_word(id, prev_tried_words):
    try:
        sqliteConnection = sqlite3.connect('log_data.db',
                                           detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        cursor = sqliteConnection.cursor()
        sqlite_insert_with_param = """INSERT INTO 'user_in_word'
                                      ('word_id','w1', 'w2', 'w3', 'w4', 'w5', 'w6') 
                                      VALUES (?, ?, ?, ?, ?, ?);"""
        if len(prev_tried_words)<6:
            for i in range(len(prev_tried_words), 7):
                prev_tried_words.append('null')
        prev_tried_words.insert(0, id)
        print('\n\n')
        print(prev_tried_words)
        print('\n\n')
        data_tuple = tuple(prev_tried_words)
        cursor.execute("INSERT INTO 'user_in_word' ('word_id','w1', 'w2', 'w3', 'w4', 'w5', 'w6') VALUES (?, ?, ?, ?, ?, ?, ?);", data_tuple)
        sqliteConnection.commit()
        print("data added successfully \n")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")


# insert into user_win_stats
def insert_user_win_stats(ind, retires):
    try:
        sqliteConnection = sqlite3.connect('log_data.db',
                                           detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        cursor = sqliteConnection.cursor()
        tmp = 0
        if retires <= 6:
            tmp = 1
        cursor.execute("INSERT INTO user_win_stats VALUES(?, ?)", (ind, tmp))
        # cursor.execute(sqlite_insert_with_param)
        sqliteConnection.commit()
        print("data added successfully \n")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")


def get_win_id():
    try:
        sqliteConnection = sqlite3.connect('log_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        cursor.execute("SELECT * FROM user_win_stats")

        return len(cursor.fetchall())
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (cursor):
            cursor.close()
            print("sqlite connection is closed")


def get_word_id():
    try:
        sqliteConnection = sqlite3.connect('log_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # get developer detail
        sqlite_select_query = """SELECT * from user_in_word"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        return len(records)

        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (cursor):
            cursor.close()
            print("sqlite connection is closed")


# insert into log
def insert_log(given_word):
    try:
        sqliteConnection = sqlite3.connect('log_data.db',
                                           detect_types=sqlite3.PARSE_DECLTYPES |
                                                        sqlite3.PARSE_COLNAMES)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        cursor = sqliteConnection.cursor()
        timestamp = get_timestamp()
        ip = get_ipaddr()
        win_id = get_win_id()
        word_id = get_word_id()
        print('timestamp', timestamp, '\nip', ip, win_id, word_id)
        lst = [timestamp, ip, given_word, win_id, word_id]
        cursor.execute("INSERT INTO log (dt, ip, selected_word, win_id, word_id) VALUES(?, ?, ?, ?, ?)", (timestamp, ip, given_word, win_id, word_id))
        sqliteConnection.commit()
        print("data added successfully \n")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")


def display_log():
        try:
            sqliteConnection = sqlite3.connect('log_data.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            # get developer detail
            # sqlite_select_query = """SELECT * from log"""
            sqlite_select_query = """SELECT * from log"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            # print(records)
            for row in records:
                print(row)

            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")


def display_words():
        try:
            sqliteConnection = sqlite3.connect('log_data.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            # get developer detail
            sqlite_select_query = """SELECT * from user_in_word"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            for row in records:
                print(row)

            cursor.close()

        except sqlite3.Error as error:
            print("Error while working with SQLite", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")


def display_stats():
    try:
        sqliteConnection = sqlite3.connect('log_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        # get developer detail
        sqlite_select_query = """SELECT * from user_win_stats"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        for row in records:
            print(row)

        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


def select_in_range(start_ts, end_ts):
    try:
        sqliteConnection = sqlite3.connect('log_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        start_ts = '2022-04-27 (18:44:44)'
        end_ts = '2022-04-27 (18:46:07)'
        # get developer detail
        # sqlite_select_query = """select *
        #        from log
        #        where dt between '2022-04-27 (18:44:44)' and '2022-04-27 (18:46:07)';
        #     """
        sqlite_select_query = """select *
                       from log
                       where dt between ? and ?;
                    """
        # select *
        # from log where
        # dt
        # between
        # '2022-04-27 (18:44:44)' and '2022-04-27 (18:46:07)';
        cursor.execute(sqlite_select_query, (start_ts, end_ts))
        records = cursor.fetchall()
        # print(records)
        for row in records:
            print(row)

        cursor.close()

    except sqlite3.Error as error:
        print("Error while working with SQLite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

if __name__ == '__main__':
    select_in_range('2022-04-27 (18:44:44)', '2022-04-27 (18:46:07)')




