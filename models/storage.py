import sqlite3
from contextlib import closing

DB_FILE = 'meetmanager.db'

def init_db():
    with closing(sqlite3.connect(DB_FILE)) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS meets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            venue TEXT,
            director TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meet_id INTEGER,
            swimmer TEXT,
            time REAL,
            FOREIGN KEY(meet_id) REFERENCES meets(id)
        )''')
        conn.commit()

def save_meet(name, date, venue, director):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO meets (name, date, venue, director) VALUES (?, ?, ?, ?)', (name, date, venue, director))
        conn.commit()
        return c.lastrowid

def get_meets():
    with closing(sqlite3.connect(DB_FILE)) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM meets ORDER BY date DESC')
        return c.fetchall()

def save_result(meet_id, swimmer, time):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO results (meet_id, swimmer, time) VALUES (?, ?, ?)', (meet_id, swimmer, time))
        conn.commit()

def get_results(meet_id):
    with closing(sqlite3.connect(DB_FILE)) as conn:
        c = conn.cursor()
        c.execute('SELECT swimmer, time FROM results WHERE meet_id=?', (meet_id,))
        return c.fetchall()

init_db()
