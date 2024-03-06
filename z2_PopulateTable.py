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
addMovie("Inception", "Christopher Nolan", 2010, "Sci-Fi")
addMovie("The Shawshank Redemption", "Frank Darabont", 1994, "Drama")
addMovie("The Godfather", "Francis Ford Coppola", 1972, "Crime")
addMovie("Pulp Fiction", "Quentin Tarantino", 1994, "Crime")
addMovie("The Dark Knight", "Christopher Nolan", 2008, "Action")