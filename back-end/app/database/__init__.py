from flask import g #Global context object (cache) stores information in memory to turn in globally available
#Acts as a global context to store data within the flask app
import sqlite3 #Provides an interface for interacting with sqlite databases

DB_URI = "main.db" #Unifrom resource identifier, it is a constant
#Singleton design pattern, only one connection to the database engine
def get_db(): #Defines function that will be used to retrieve a database connection
        db = getattr(g, "_database", None) #Uses getattr function to retrieve the att named _database from the g object, if it doesn't exist, it returns None
        if not db: #Checks if the db variable is None, indicating that a database connection hasn't been established yet.
                db = g._database = sqlite3.connect(DB_URI)#If no connection exists, it creates a new database connection using sqlite3.connect(DB_URI). The connection is stored in both the db variable and in the _database attribute of the g context
        return db #Returns the database connection object.

#We get database from context, if there is none, we establish a connection and send it to the context in the form of the attribute _database, and to whatever piece of code called the function, as db. 