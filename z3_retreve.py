import sqlite3

conn= sqlite3.connect('databaseFile.db')
curse = conn.cursor()

#Reads all table
curse.execute("SELSECT * FROM movies")
print(curse.fetchall())