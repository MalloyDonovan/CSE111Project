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
        ###ASSIGN QUERY RESULTS TO LABEL
        results["text"] = '\n'.join(''.join(tup) for tup in rows)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def search(_conn):
    _conn.execute("BEGIN")
    try:
        input = entrySearch.get()
        sql = ''' 
                SELECT g_title FROM Games
                WHERE g_title LIKE '%{}%'
                LIMIT 20;
            '''.format(input)
        _conn.execute(sql)
        cur = _conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        ###ASSIGN QUERY RESULTS TO LABEL
        results["text"] = '\n'.join(''.join(tup) for tup in rows)
        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)


######CAN BE OPTIMIZED BY TAKING THE LIST 
def handle_click_q1(event):
    database = r"videogames.db"
    conn = openConnection(database)
    q1(conn)
    closeConnection(conn, database)


###Search related methods##########################################

def handle_click_search(event):
    entrySearch.grid(row=1, column=2, sticky="s")
    confirmSearch.grid(row=2, column=2, sticky="n")

def executeSearch(event):
    database = r"videogames.db"
    conn = openConnection(database)
    search(conn)
    closeConnection(conn, database)
    entrySearch.delete(0, 20)
    entrySearch.grid_forget()
    confirmSearch.grid_forget()

##################################################################


###SignIn related methods##########################################

def checkCred(event):
    if entryCred.get() == 'password':
       entryCred.delete(0, 20)
       entryCred.grid_forget()
       confirmCred.grid_forget()
       signOut.grid(row=4, column=0)
       adminMessage.grid(row=3, column =0, sticky = "s")
     
def signInProc(event):
    signIn.grid_forget()
    entryCred.grid(row=1, column=2, sticky="s")
    confirmCred.grid(row=2, column=2, sticky="n")

def signOutProc(event):
    adminMessage.grid_forget()
    signOut.grid_forget()
    signIn.grid(row=4, column=0)

##################################################################
    



#Creates Tkinter window
window = tk.Tk()
window.resizable(False, False)
window.columnconfigure([0, 1, 2, 3, 4], minsize=160)
window.rowconfigure([0, 1, 2, 3, 4], minsize=90)

results = tk.Label(text="Video game database")
adminMessage = tk.Label(text="Welcome system administrator!")

entryCred = tk.Entry(fg="white", bg="black", width=40)
entrySearch = tk.Entry(fg="white", bg="black", width=40)

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

searchButton = tk.Button(
    text="Search for title",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

confirmSearch = tk.Button(
    text="Confirm",
    width=25,
    height=5,
    bg="black",
    fg="white",
)



results.grid(row=2, column=4)
button.grid(row=0, column=0)
signIn.grid(row=4, column = 0)
searchButton.grid(row=1, column=0)


button.bind("<Button-1>", handle_click_q1)
searchButton.bind("<Button-1>", handle_click_search)

signIn.bind("<Button-1>", signInProc)
signOut.bind("<Button-1>", signOutProc)


confirmCred.bind("<Button-1>", checkCred)
confirmSearch.bind("<Button-1>", executeSearch)

window.mainloop()