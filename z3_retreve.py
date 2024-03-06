import sqlite3

conn= sqlite3.connect('databaseFile.db')
curse = conn.cursor()

curse.execute("SELECT * FROM sqlite_master WHERE type='table'")
#Reads all table
print("This gives us the tables in the database")
print(curse.fetchall())
print()

#Reads all table
curse.execute("SELECT * FROM movies")
print("This gives us everything from the movie table")
print(curse.fetchall())

#This pulls all colums from table
curse.execute("PRAGMA table_info({});".format("movies"))
#this prints eveything about the coloums
colums =curse.fetchall()
print("This is all data about the colums")
print(colums)
print()

#This prints just the names
colsNames = [colum[1] for colum in colums]
print ("This just prints the colums names from the table movies")
print(colsNames)
print()

#This prints movies in a certain years
curse.execute("SELECT title, director, year FROM movies WHERE year = 1970")
print("List all movies from 1970:")
print(curse.fetchall())
print()