import sqlite3

from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('tests.db')
        return con
    except Error:
        print(Error)

def sql_tables():
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE test(test_id integer PRIMARY KEY, subject text, answer_keys text)")
    cursorObj.execute("CREATE TABLE submissions(test_id integer, scantron_id integer, scantron_url text, name text, \
                      subject text, score integer, result text, PRIMARY KEY(test_id, scantron_id))")
    con.commit()

def insert_test(entities):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO test(test_id, subject, answer_keys) VALUES(?, ?, ?)', entities)
    con.commit()

def insert_submission(entities):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        'INSERT INTO submissions(test_id, scantron_id, scantron_url, name, subject, score, result) VALUES(?, ?, ?, ?, ?, ?, ?)', entities)
    con.commit()

def fetch_test_keys(test_id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        'SELECT answer_keys from test WHERE test_id = {}'.format(test_id))
    rows = cursorObj.fetchall()
    return rows[0][0]

def fetch_test(test_id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        'SELECT * from test WHERE test_id = {}'.format(test_id))
    rows = cursorObj.fetchall()
    return rows[0]

def get_all_submissions(test_id):
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(
        'SELECT * from submissions WHERE test_id={}'.format(test_id))
    rows = cursorObj.fetchall()
    return rows

def cleanup():
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute("DROP TABLE test")
    cursorObj.execute("DROP TABLE submissions")
