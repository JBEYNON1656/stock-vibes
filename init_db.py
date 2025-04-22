import sqlite3

#connect to / create database file
conn = sqlite3.connect("stock__vibe_data.db")
c = conn.cursor()

#create table if doesn't already exist
c.execute('''
    CREATE TABLE IF NOT EXISTS stocks (
        symbol TEXT,
        price REAL,
        timestamp TEXT,
        news_title TEXT,
        news_sentiment TEXT         
    )
''')

conn.commit()
conn.close()