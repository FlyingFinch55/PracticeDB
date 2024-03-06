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

#Templet for add movies and do not run it again it is already in the table
#addMovie("StarWars", "John Williams", 1970, "Sci-fi")


