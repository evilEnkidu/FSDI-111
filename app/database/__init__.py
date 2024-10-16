from flask import g # global context object (cache) stores information in memory to turn in globally available
import sqlite3

DB_URI = "main.db" #unifrom resource identifier, it is a constant
#singleton design pattern, only one connection to the database engine
def get_db():
        db = getattr(g, "_database", None)
        if not db:
                db = g._database = sqlite3.connect(DB_URI)
        return db