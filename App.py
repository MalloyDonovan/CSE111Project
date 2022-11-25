import tkinter as tk
import sqlite3
from sqlite3 import Error

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    #with conn:
        #dropTable(conn)
        #createTable(conn)
        #populateTable(conn)

        #Q1(conn)
        #Q2(conn)
        #Q3(conn)
        #Q4(conn)
        #Q5(conn)

    closeConnection(conn, database)

#Creates Tkinter window
window = tk.Tk()
title = tk.Label(text="Video game database")
title.pack()
window.mainloop()
print("test")