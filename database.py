import sqlite3

def get_db_connection():
    conn = sqlite3.connect('youtube_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            transcript TEXT,
            summary TEXT
        )
    ''')
    conn.commit()
    return conn, c
