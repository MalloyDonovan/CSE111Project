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
                    SELECT * FROM Games
                    WHERE g_title = '{}'
                '''.format(temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingDevs == True:
            sql = ''' 
                    SELECT * FROM gameDevs
                    WHERE gdev_developer = '{}'
                '''.format(temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingData == True:
            sql = ''' 
                    SELECT * FROM gameData
                    WHERE gd_name = '{}'
                '''.format(temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

        detailsDisplay["text"] = rows

        #Remove not relevant items, add a back button later
        if loggedin == True:                
            deleteEntry.grid(row=4, column = 3)
            updateEntry.grid(row=4, column = 2)
        inspectBackbtn.grid(row=0, column=1)
        clearResults()
        leftPage.grid_remove()
        rightPage.grid_remove()

        detailsDisplay.grid(row=2, column=2)

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def deleteDB(_conn):
    _conn.execute("BEGIN")
    try:
        if searchingGames == True:
            sql = ''' 
                    Delete FROM Games
                    WHERE g_title = '{}'
                '''.format(temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingDevs == True:
            sql = ''' 
                    DELETE FROM gameDevs
                    WHERE gdev_developer = '{}'
                '''.format(temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingData == True:
            sql = ''' 
                    DELETE FROM gameData
                    WHERE gd_name = '{}'
                '''.format(temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

        detailsDisplay["text"] = rows

        clearResults()
        leftPage.grid_remove()
        rightPage.grid_remove()
        updateEntry.grid_remove()
        deleteEntry.grid_remove()
        inspectBackbtn.grid_remove()
        detailsDisplay.grid_remove()
        

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def updateDB(_conn):
    try:
        if searchingGames == True:
            sql = ''' 
                    UPDATE Games
                    SET {} = '{}'
                    WHERE g_title = '{}'
                '''.format(toModify.get(), theModification.get(), temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingDevs == True:
            sql = ''' 
                    UPDATE gameDevs
                    SET {} = '{}'
                    WHERE gdev_developer = '{}'
                '''.format(toModify.get(), theModification.get(), temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
        elif searchingData == True:
            sql = ''' 
                    UPDATE gameData
                    SET {} = '{}'
                    WHERE gd_name = '{}'
                '''.format(toModify.get(), theModification.get(), temporaryString["text"])
            _conn.execute(sql)
            cur = _conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

            toModify.delete(0, 20)
            theModification.delete(0, 20)
    

        _conn.execute("COMMIT")
        print("success")
    except Error as e:
        _conn.execute("ROLLBACK")
        print(e)

def insertDB(_conn):
    try:
        if searchingGames == True:
            sql = ''' 
                    INSERT INTO Games(g_id, g_title, g_mainStory, g_mainPlus, g_Completionist, g_allStyles, g_coop, g_versus, g_type, g_developers, g_publishers, g_platforms, g_genres, g_releaseNA, g_releaseEU, g_releaseJP)
                    VALUES (68032,'{}',0,0,0,0,0,0,'None','None','None','None','None','None','None','None')
                '''.format(insertEntry.get())
            _conn.execute(sql)
        elif searchingDevs == True:
            sql = ''' 
                    INSERT INTO gameDevs (gdev_developer, gdev_city, gdev_administrative_division, gdev_country, gdev_est, gdev_notable)
                    VALUES ('{}', 'None', 'None', 'None', 'None', 'None')
                '''.format(insertEntry.get())
            _conn.execute(sql)
        elif searchingData == True:
            sql = ''' 
                    INSERT INTO gameData (gd_name, gd_platform, gd_date, gd_score, gd_uscore, gd_developer, gd_genre, gd_players, gd_critics, gd_users)
                    VALUES ('{}', 'None', 'None', 0, 0, 'None', 'None', 0, 0, 0)
                '''.format(insertEntry.get())
            _conn.execute(sql)

        insertEntry.delete(0, 20)

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
    if 0 <= 7 < len(results["text"].split('\n')):
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
        temporaryString["text"] = event.widget["text"]
        details(conn)
        closeConnection(conn, database)

def inspect_back(event):
    inspectBackbtn.grid_remove()
    detailsDisplay.grid_remove()
    deleteEntry.grid_remove()
    updateEntry.grid_remove()
    executeSearch(event)

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
        insertEntryButton.grid(row=3, column=0)
        adminMessage.grid(row=3, column =0, sticky = "s")

     
def signInProc(event):
    signIn.grid_forget()
    entryCred.grid(row=1, column=2, sticky="s")
    confirmCred.grid(row=2, column=2, sticky="n")

def signOutProc(event):
    global loggedin
    loggedin = False
    adminMessage.grid_forget()
    insertEntryButton.grid_remove()
    signOut.grid_forget()
    signIn.grid(row=4, column=0)


def listColumns(event):
        if searchingGames == True:
            toBeModified["text"] = "Enter catrgory to modify: \n g_title \n g_genres"

        elif searchingDevs == True:
            toBeModified["text"] = "Enter catrgory to modify: \n gdev_developer \n gdev_city"

        elif searchingData == True:
            toBeModified["text"] = "Enter catrgory to modify: \n gd_name \n gd_platform"

        toBeModified.grid(row=2, column =2)
        toModify.grid(row=3, column=2)
        toModifyBtn.grid(row=4, column=2)
        
        clearResults()
        leftPage.grid_remove()
        rightPage.grid_remove()
        updateEntry.grid_remove()
        deleteEntry.grid_remove()
        inspectBackbtn.grid_remove()
        detailsDisplay.grid_remove()

def promptModification(event):
    toModify.grid_forget()
    toModifyBtn.grid_remove()
    toBeModified["text"] = "Enter modification"
    theModification.grid(row=3, column=2)
    theModificationBtn.grid(row=4, column=2)

def updateProcess(event):
        theModification.grid_forget()
        theModificationBtn.grid_remove()
        toBeModified.grid_remove()
        database = r"videogames.db"
        conn = openConnection(database)
        updateDB(conn)
        closeConnection(conn, database)

def deleteProcess(event):
        database = r"videogames.db"
        conn = openConnection(database)
        deleteDB(conn)
        closeConnection(conn, database)

def selectInsertType(event):
    insertTypeText["text"] = "Select type to insert"
    insertTypeText.grid(row=2,column=3)
    insertType1.grid(row=3, column=2)
    insertType2.grid(row=3, column=3)
    insertType3.grid(row=3, column=4)

def Type1(event):
    global searchingData
    global searchingDevs
    global searchingGames 
    searchingData = False
    searchingDevs = False
    searchingGames = True
    insertPrompt()

def Type2(event):
    global searchingData
    global searchingDevs
    global searchingGames 
    searchingData = False
    searchingDevs = True
    searchingGames = False
    insertPrompt()


def Type3(event):
    global searchingData
    global searchingDevs
    global searchingGames 
    searchingData = True
    searchingDevs = False
    searchingGames = False
    insertPrompt()

def insertPrompt():
    insertType1.grid_remove()
    insertType2.grid_remove()
    insertType3.grid_remove()
    insertTypeText.grid_remove()
    insertPromptText["text"] = "Enter name of entry"
    insertPromptText.grid(row=2, column = 2)
    insertEntry.grid(row=3, column=2)
    insertConfirm.grid(row=4, column=2)

def insertProcess(event):
        insertPromptText.grid_remove()
        insertConfirm.grid_remove()
        insertEntry.grid_remove()
        database = r"videogames.db"
        conn = openConnection(database)
        insertDB(conn)
        closeConnection(conn, database)


##################################################################
    





####################################################################


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

temporaryString = tk.Label()
detailsDisplay = tk.Label()
toBeModified = tk.Label()
insertTypeText = tk.Label()
insertPromptText = tk.Label()

entryCred = tk.Entry(bg="white", width=40)
entrySearch = tk.Entry(bg="white", width=30)
toModify = tk.Entry(bg="white", width=30)
theModification = tk.Entry(bg="white", width=30)
insertEntry  = tk.Entry(bg="white", width=30)


signIn = tk.Button( text="Are you an admin? Sign in!", width=25, height=5, bg="white")
signOut = tk.Button( text="Sign out", width=25, height=5, bg="white")
confirmCred = tk.Button(text="Confirm", width=25, height=5, bg="white")
updateEntry = tk.Button(text="Update", width=25, height=5, bg="Green")
deleteEntry = tk.Button(text="Delete", width=25, height=5, bg="Red")
insertEntryButton = tk.Button(text="Insert", width=25, height=5, bg="Yellow")
insertConfirm = tk.Button(text="Confirm", width=25, height=5, bg="white")
toModifyBtn = tk.Button(text="Confirm", width=25, height=5, bg="white")
theModificationBtn = tk.Button(text="Confirm", width=25, height=5, bg="white")

insertType1 = tk.Button(text="Games", width=10, height=2, bg="white")
insertType2 = tk.Button(text="gameDev", width=10, height=2, bg="white")
insertType3 = tk.Button(text="gameData", width=10, height=2, bg="white")

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

inspectBackbtn = tk.Button(text = "Back", width=10, height=2, bg="white")

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

updateEntry.bind("<Button-1>", listColumns)
deleteEntry.bind("<Button-1>", deleteProcess)
insertEntryButton.bind("<Button-1>", selectInsertType)
insertConfirm.bind("<Button-1>", insertProcess)
toModifyBtn.bind("<Button-1>", promptModification)
theModificationBtn.bind("<Button-1>", updateProcess)

insertType1.bind("<Button-1>", Type1)
insertType2.bind("<Button-1>", Type2)
insertType3.bind("<Button-1>", Type3)



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
inspectBackbtn.bind("<Button-1>", inspect_back)

window.mainloop()