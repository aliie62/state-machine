from utilities.randomiser import randomiser
from models.state import StateModel
import string
import os
import sqlite3

DATABASE_URI = os.environ.get('DATABASE_URI','data.db')

def create_table():
    connection = sqlite3.connect('data.db')
    cursor= connection.cursor()
    query='CREATE TABLE IF NOT EXISTS states (id INT PRIMARY KEY, name TEXT, dest_1 INT,dest_2 INT,dest_3 INT,is_active boolean)'
    cursor.execute(query)
    connection.commit()
    connection.close()

def empty_table():
    connection = sqlite3.connect('data.db')
    cursor= connection.cursor()
    cursor.execute('DELETE FROM states')
    connection.commit()
    connection.close()

def fill_table():
    letters_execpt_z=string.ascii_uppercase[:-1]
    try:
        for i,letter in enumerate(letters_execpt_z):
            d1 = randomiser()
            d2 = randomiser()
            d3 = randomiser()
            if letter=='A':
                is_active=True
            else:
                is_active=False
            state=StateModel(i+1,letter,d1,d2,d3,is_active)
            
            state.insert()
        state=StateModel(26,'Z',1,1,1,False)
        state.insert()
    except:
        raise Exception('Error in populating the table.')
