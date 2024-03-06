import sqlite3

conn= sqlite3.connect('databaseFile.db')
curse = conn.cursor()

#movies is table name
curse.execute("""
              CREATE TABLE IF NOT EXISTS movies (
              id INTEGER PRIMARY KEY,
              title TEXT,
              director TEXT,
              year INTEGER,
              gen TEXT )
              """)
#Table should be created with table and attrabultes
