import sqlite3
import os

SM_DATABASE_URI = os.environ.get('SM_DATABASE_URI')

class StateModel():
    _tablename = 'states'


    def __init__(self,_id:int,name:str,dest_1:int,dest_2:int,dest_3:int, is_active:bool) -> None:
        self.id = _id
        self.name = name
        self.dest_1 = dest_1
        self.dest_2 = dest_2
        self.dest_3 = dest_3
        self.is_active = is_active
    
    @classmethod
    def get_current_state(cls)->"StateModel":
        connection = sqlite3.connect(SM_DATABASE_URI)
        cursor = connection.cursor()
        query = f"SELECT * FROM {cls._tablename} where is_active=True"
        row = cursor.execute(query).fetchone()
        state = StateModel(*row)
        connection.close()
        return state

    @classmethod
    def get_state_by_id(cls,state_id)->"StateModel":
        connection = sqlite3.connect(SM_DATABASE_URI)
        cursor = connection.cursor()
        query = f"SELECT * FROM {cls._tablename} where id=?"
        row = cursor.execute(query,(state_id,)).fetchone()
        state = StateModel(*row)
        connection.close()
        return state

    def update(self) -> None:
        connection = sqlite3.connect(SM_DATABASE_URI)
        cursor = connection.cursor()
        query = f"UPDATE {StateModel._tablename} SET is_active=? WHERE id=?"
        cursor.execute(query,(self.is_active,self.id))
        connection.commit()
        connection.close()
    
    def insert(self)-> None:
        connection = sqlite3.connect(SM_DATABASE_URI)
        cursor = connection.cursor()
        query = f"INSERT INTO {StateModel._tablename} VALUES (?,?,?,?,?,?)"
        cursor.execute(query,(self.id,self.name,self.dest_1,self.dest_2,self.dest_3,self.is_active))
        connection.commit()
        connection.close()