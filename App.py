import tkinter as tk
import sqlite3
from sqlite3 import Error

searchingData = False
searchingDevs = False
searchingGames = False
loggedin = False


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


def search(_conn):
    _conn.execute("BEGIN")
    try:
        if searchingGames == True:
            input = entrySearch.get()
            sql = ''' 
                    SELECT g_title FROM Games
                    WHERE g_title LIKE '%{}%'
                    LIMIT 8 OFFSET {};
                '''.format(input, Offset)
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingDevs == True:
            input = entrySearch.get()
            sql = ''' 
                    SELECT gdev_developer FROM gameDevs
                    WHERE gdev_developer LIKE '%{}%'
                    LIMIT 8 OFFSET {};
                '''.format(input, Offset)
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingData == True:
            input = entrySearch.get()
            sql = ''' 
                    SELECT gd_name FROM gameData
                    WHERE gd_name LIKE '%{}%'
                    LIMIT 8 OFFSET {};
                '''.format(input, Offset)
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        ###ASSIGN QUERY RESULTS TO LABEL

        results["text"] = '\n'.join(''.join(tup) for tup in rows)
       
        if 0 <= 0 < len(results["text"].split('\n')):
            result1.grid(row=0, column=3)
            result1["text"] = results["text"].split('\n')[0]

        if 0 <= 1 < len(results["text"].split('\n')):
            result2.grid(row=0, column=4)
            result2["text"] = results["text"].split('\n')[1]

        if 0 <= 2 < len(results["text"].split('\n')):
            result3.grid(row=1, column=3)
            result3["text"] = results["text"].split('\n')[2]

        if 0 <= 3 < len(results["text"].split('\n')):
            result4.grid(row=1, column=4)
            result4["text"] = results["text"].split('\n')[3]

        if 0 <= 4 < len(results["text"].split('\n')):
            result5.grid(row=2, column=3)
            result5["text"] = results["text"].split('\n')[4]

        if 0 <= 5 < len(results["text"].split('\n')):
            result6.grid(row=2, column=4)
            result6["text"] = results["text"].split('\n')[5]

        if 0 <= 6 < len(results["text"].split('\n')):
            result7.grid(row=3, column=3)
            result7["text"] = results["text"].split('\n')[6]

        if 0 <= 7 < len(results["text"].split('\n')):
            result8.grid(row=3, column=4)
            result8["text"] = results["text"].split('\n')[7]
            leftPage.grid(row=4, column=3)
            rightPage.grid(row=4, column=4)


        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def details(_conn):
    _conn.execute("BEGIN")
    try:
        if searchingGames == True:
            sql = ''' 
                    SELECT * FROM games
                    WHERE g_title = '{}'
                '''.format(result1["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingDevs == True:
            sql = ''' 
                    SELECT * FROM gameDevs
                    WHERE gdev_developer = '{}'
                '''.format(result1["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingData == True:
            sql = ''' 
                    SELECT * FROM gameData
                    WHERE gd_name = '{}'
                '''.format(result1["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

        detailsDisplay["text"] = rows

        #Remove not relevant items, add a back button later
        clearResults()
        leftPage.grid_remove()
        rightPage.grid_remove()

        detailsDisplay.grid(row=2, column=2)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)


###Search related methods##########################################

def handle_games_search(event):
    detailsDisplay.grid_remove()
    global Offset
    global searchingGames 
    global searchingDevs
    global searchingData
    searchingGames = True
    searchingDevs = False
    searchingData = False
    Offset = 0
    entrySearch.delete(0, 20)
    entrySearch.grid(row=0, column=1, padx=5, sticky="n")
    confirmSearch.grid(row=0, column=2, sticky="nw")
    clearResults()
    leftPage.grid_remove()
    rightPage.grid_remove()

def handle_dev_search(event):
    detailsDisplay.grid_remove()
    global Offset
    global searchingGames 
    global searchingDevs
    global searchingData
    searchingGames = False
    searchingDevs = True
    searchingData = False
    Offset = 0
    entrySearch.delete(0, 20)
    entrySearch.grid(row=0, column=1, padx=5, sticky="n")
    confirmSearch.grid(row=0, column=2, sticky="nw")
    clearResults()
    leftPage.grid_remove()
    rightPage.grid_remove()

def handle_data_search(event):
    detailsDisplay.grid_remove()
    global Offset
    global searchingGames 
    global searchingDevs
    global searchingData
    searchingGames = False
    searchingDevs = False
    searchingData = True
    Offset = 0
    entrySearch.delete(0, 20)
    entrySearch.grid(row=0, column=1, padx=5, sticky="n")
    confirmSearch.grid(row=0, column=2, sticky="nw")
    clearResults()
    leftPage.grid_remove()
    rightPage.grid_remove()

def executeSearch(event):
    database = r"videogames.db"
    conn = openConnection(database)
    search(conn)
    closeConnection(conn, database)
    entrySearch.grid_forget()
    confirmSearch.grid_forget()

def incrementOffset(event):
    global Offset
    Offset += 8
    clearResults()
    database = r"videogames.db"
    conn = openConnection(database)
    search(conn)
    closeConnection(conn, database)

def decrementOffset(event):
    global Offset
    if Offset > 7:
        Offset += -8
        clearResults()
        database = r"videogames.db"
        conn = openConnection(database)
        search(conn)
        closeConnection(conn, database)

def inspect(event):
        database = r"videogames.db"
        conn = openConnection(database)
        details(conn)
        closeConnection(conn, database)

def clearResults():
    result1.grid_remove()
    result2.grid_remove()
    result3.grid_remove()
    result4.grid_remove()
    result5.grid_remove()
    result6.grid_remove()
    result7.grid_remove()
    result8.grid_remove()

##################################################################


###SignIn related methods##########################################

def checkCred(event):
    if entryCred.get() == 'password':
        global loggedin
        loggedin = True
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
    



#Global Variables

Offset = 0

#Creates Tkinter window

window = tk.Tk()
window.title("Game Database Search")
window.resizable(False, False)
window.columnconfigure([0, 1, 2, 3, 4], minsize=160)
window.rowconfigure([0, 1, 2, 3, 4], minsize=90)

results = tk.Label(text="Video game database")
adminMessage = tk.Label(text="Welcome system administrator!")
detailsDisplay = tk.Label()

entryCred = tk.Entry(bg="white", width=40)
entrySearch = tk.Entry(bg="white", width=30)


signIn = tk.Button( text="Are you an admin? Sign in!", width=25, height=5, bg="white")
signOut = tk.Button( text="Sign out", width=25, height=5, bg="white")
confirmCred = tk.Button(text="Confirm", width=25, height=5, bg="white")
searchButton = tk.Button(text="Search for title",width=25,height=5, bg="white")
searchDev = tk.Button(text="Search for developer",width=25,height=5, bg="white")
searchdata = tk.Button(text="Retrieve game data",width=25,height=5, bg="white")
confirmSearch = tk.Button(text="Confirm", width=10, height=2, bg="white")

result1 = tk.Button(width=25, height=5, bg="white")
result2 = tk.Button(width=25, height=5, bg="white")
result3 = tk.Button(width=25, height=5, bg="white")
result4 = tk.Button(width=25, height=5, bg="white")
result5 = tk.Button(width=25, height=5, bg="white")
result6 = tk.Button(width=25, height=5, bg="white")
result7 = tk.Button(width=25, height=5, bg="white")
result8 = tk.Button(width=25, height=5, bg="white")

leftPage = tk.Button(text = "<-", width=10, height=2, bg="white")
rightPage = tk.Button(text = "->", width=10, height=2, bg="white")


##Placeholder##
'''
result1.grid(row=0, column=3)
result2.grid(row=0, column=4)
result3.grid(row=1, column=3)
result4.grid(row=1, column=4)
result5.grid(row=2, column=3)
result6.grid(row=2, column=4)
result7.grid(row=3, column=3)
result8.grid(row=3, column=4)

leftPage.grid(row=4, column=3)
rightPage.grid(row=4, column=4)
'''



#Old results display
#results.grid(row=2, column=4)
signIn.grid(row=4, column = 0)
searchButton.grid(row=0, column=0)
searchDev.grid(row=1,column=0)
searchdata.grid(row=2,column=0)

searchButton.bind("<Button-1>", handle_games_search)
searchDev.bind("<Button-1>", handle_dev_search)
searchdata.bind("<Button-1>", handle_data_search)


signIn.bind("<Button-1>", signInProc)
signOut.bind("<Button-1>", signOutProc)


confirmCred.bind("<Button-1>", checkCred)
confirmSearch.bind("<Button-1>", executeSearch)

leftPage.bind("<Button-1>", decrementOffset)
rightPage.bind("<Button-1>", incrementOffset)

result1.bind("<Button-1>", inspect)
result2.bind("<Button-1>", inspect)
result3.bind("<Button-1>", inspect)
result4.bind("<Button-1>", inspect)
result5.bind("<Button-1>", inspect)
result6.bind("<Button-1>", inspect)
result7.bind("<Button-1>", inspect)
result8.bind("<Button-1>", inspect)

window.mainloop()