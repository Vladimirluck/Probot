import sqlite3

def get_connection():
    conn = sqlite3.connect('real_estate.db')
    return conn
