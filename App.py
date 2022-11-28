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


def q1(_conn):
    _conn.execute("BEGIN")
    try:
        sql = ''' 
                SELECT g_title FROM Games
                WHERE strftime('%Y', g_releaseNA) = '2000' AND g_mainStory > 30
                LIMIT 20;
            '''
        _conn.execute(sql)
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        ###ASSIGN QUERY RESULTS TO BUTTON
        results["text"] = '\n'.join(''.join(tup) for tup in rows)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)



######CAN BE OPTIMIZED BY TAKING THE LIST 
def handle_click(event):
    database = r"videogames.db"

    # create a database connection
    conn = openConnection(database)
    q1(conn)
    closeConnection(conn, database)



#Creates Tkinter window
window = tk.Tk()
results = tk.Label(text="Video game database")

button = tk.Button(
    text="Click to show titles from 2000!",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

results.pack()
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()