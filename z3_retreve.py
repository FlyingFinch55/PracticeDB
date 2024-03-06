import sqlite3

conn= sqlite3.connect('databaseFile.db')
curse = conn.cursor()

curse.execute("SELECT * FROM sqlite_master WHERE type='table'")
#Reads all table
print(curse.fetchall())
print()

#Reads all table
curse.execute("SELECT * FROM movies")
print(curse.fetchall())