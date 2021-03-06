import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE


#command = ""          put SQL statement in this string
#c.execute(command)    run SQL statement

#courses
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)") 

with open('courses.csv') as csvfile:
    dict_reader = csv.DictReader(csvfile)
    for row in dict_reader:
        command = 'INSERT INTO courses VALUES("'+str(row["code"])+'",'+str(row['mark'])+","+str(row['id'])+");"
        c.execute(command)

#peeps
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")

with open('peeps.csv') as csvfile:
    dict_reader = csv.DictReader(csvfile)
    for row in dict_reader:
        command = 'INSERT INTO peeps VALUES("'+str(row["name"])+'",'+str(row['age'])+","+str(row['id'])+");"
        c.execute(command)

#==========================================================
db.commit() #save changes
db.close()  #close database
