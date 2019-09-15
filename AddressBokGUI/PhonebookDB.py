import mysql.connector

db = mysql.connector.connect(host="localhost",  # your host
                            user="root",       # username
                            passwd="Kvmz5687mnb1210!",     # password
                            db="phonebook")   # name of the database

# Create a Cursor object to execute queries.

cur = db.cursor()


#CRUD
def createPerson(name, phone, email, age):

    cur.execute(f"INSERT INTO contact VALUES (0,'{name}','{phone}','{email}','{age}')")
    db.commit()

def searchPerson(name):

    cur.execute(f"SELECT * FROM contact WHERE Name = '{name}'")
    dbList = []
    for row in cur.fetchall():
        dbList += row[1:]
    return dbList

# def updatePerson():

#def deletePerson():


