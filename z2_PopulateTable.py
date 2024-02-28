import sqlite3

conn= sqlite3.connect('databaseFile.db')
curse = conn.cursor()

def addMovie(title, director, year, gen):

    curse.execute("""
                INSERT INTO movies(title, director, year, gen) 
                VALUES (?,?,?,?)""", (title,director,year,gen)

    )
    conn.commit()
    print("Movie added :)")

addMovie("StarWars", "John Williams", 1970, "Sci-fi")