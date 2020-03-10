import sqlite3

#opens a database file, creates a new file if one doesn't exist exist
db= sqlite3.connect('dataFile')
cursor = db.cursor()

#creates a table if one does not exist, otherwise does nothing
def createTable():       
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS trade_data(id INTEGER PRIMARY KEY, rsi REAL) ''')
        db.commit()
    except:
        pass



def calculateMovingAverage(period, data):
    average = 0
    for x in range(period):
        average = average + data.get[x-1]

    return average/ period


def calculateRsi(data):
    existingData = None
    try:
        cursor.execute(''' SELECT rsi FROM trade_data ORDER BY id DESC LIMIT 1''')
        existingData = cursor.fetchone()
    except:
        pass

    if existingData:
        
        pass 
    else:

        pass

