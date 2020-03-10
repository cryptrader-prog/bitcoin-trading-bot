import sqlite3

#opens a database file, creates a new file if one doesn't exist exist
db= sqlite3.connect('dataFile')

#creates a table if one does not exist, otherwise does nothing
def createTable():    
    cursor = db.cursor()
    try:
        cursor.execute('''SELECT id FROM trade_data''')
        data = cursor.fetchone()
    except:
        pass
    if(data):
        try:
            cursor.execute('''CREATE TABLE trade_data(id INTEGER PRIMARY KEY, rsi REAL) ''')
            db.commit()
        except:
            pass
    else:
        pass



def calculateMovingAverage(period, data):
    average = 0
    for x in range(period):
        average = average + data.get[x-1]

    return average/ period