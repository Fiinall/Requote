import sqlite3
from datetime import datetime

connection = sqlite3.connect("rq.db")
cursor = connection.cursor()


def createtable():
    connection = sqlite3.connect("rq.db")
    cursor = connection.cursor()
    query = """CREATE TABLE IF NOT EXISTS quotebook (
    ID INT,
    content TEXT, 
    topic TEXT,
    author TEXT,
    createdtime TEXT)"""
    cursor.execute(query)

def add_quote_db(request_data):
    connection = sqlite3.connect("rq.db")
    cursor = connection.cursor()
    cursor.execute("select * from quotebook")
    datanumber = len(cursor.fetchall())
    new_id = datanumber + 1
    query = """
    Insert into quotebook Values(?,?,?,?,?)
    """
    adding_time = datetime.strftime(datetime.now(),"%Y %B %A %X")
    cursor.execute(query,(new_id,request_data["content"],request_data["topic"],request_data["author"],adding_time))
    connection.commit()

def delete_quote_db(id): # Deleting via id of quote
    connection = sqlite3.connect("rq.db")
    cursor = connection.cursor()
    cursor.execute("Delete From quotebook where ID = ?",(id,))
    connection.commit()

createtable()

