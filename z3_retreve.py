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

#This pulls all colums from table
curse.execute("PRAGMA table_info({});".format("movies"))
#this prints eveything about the coloums
colums =curse.fetchall()
print(colums)
print()

#This prints just the names
colsNames = [colum[1] for colum in colums]
print(colsNames)