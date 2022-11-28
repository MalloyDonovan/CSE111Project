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

def checkCred(event):
    if entryCred.get() == 'password':
       entryCred.pack_forget()
       confirmCred.pack_forget()
       adminMessage.pack()
       signOut.pack()
       


def signInProc(event):
    signIn.pack_forget()
    entryCred.pack()
    confirmCred.pack()

def signOutProc(event):
    adminMessage.pack_forget()
    signOut.pack_forget()
    signIn.pack()

    



#Creates Tkinter window
window = tk.Tk()
window.resizable(width=True, height=True)
results = tk.Label(text="Video game database")
adminMessage = tk.Label(text="Welcome system administrator!")

button = tk.Button(
    text="Click to show titles from 2000!",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

signIn = tk.Button(
    text="Are you an admin? Sign in!",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

signOut = tk.Button(
    text="Sign out",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

confirmCred = tk.Button(
    text="Confirm",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

entryCred = tk.Entry(fg="white", bg="black", width=50)

results.pack()
button.pack()
signIn.pack()


button.bind("<Button-1>", handle_click)
signIn.bind("<Button-1>", signInProc)
signOut.bind("<Button-1>", signOutProc)
confirmCred.bind("<Button-1>", checkCred)
window.mainloop()