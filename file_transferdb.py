import sqlite3
import time
import datetime



def openDB():
    connection = sqlite3.connect("file_transfer.db")
    c = connection.cursor()
    sql = "SELECT * FROM file_check WHERE filename = ?"

    wordUsed = 'license.txt'




def readData():
    for row in c.execute(sql, [(wordUsed)]):
        print row

def tableCreate():
  c.execute("CREATE TABLE file_check(ID INT, filename TEXT, unix REAL, datestamp TEXT, keyword TEXT, value REAL)")



idfordb = 1
filename = 'gem.txt'
keyword = 'File Check'
value = 7



def dataEntry():
    date = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    c.execute("INSERT INTO file_check (ID, filename, unix, datestamp, keyword, value) VALUES (?, ?, ?, ?, ?, ?)",
              (idfordb, filename, time.time(), date, keyword, value))
    connection.commit()



    


