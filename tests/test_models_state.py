import unittest
import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.state import StateModel

SM_DATABASE_URI = os.environ.get('SM_DATABASE_URI')
os.remove(SM_DATABASE_URI)
connection = sqlite3.connect(SM_DATABASE_URI)
cursor= connection.cursor()
query='CREATE TABLE states (id INT PRIMARY KEY, name TEXT, dest_1 INT,dest_2 INT,dest_3 INT,is_active boolean)'
cursor.execute(query)
connection.commit()
connection.close()

class RandomiserTestCase(unittest.TestCase):

    def setUp(self):
        self.state1 = StateModel(1,"A",5,8,10,True)
        self.state2 = StateModel(2,"B",26,14,4,False)
        
    def test_1_insert(self):
        self.state1.insert()
        self.state2.insert()
        connection = sqlite3.connect(SM_DATABASE_URI)
        cursor= connection.cursor()
        count = cursor.execute('SELECT COUNT(*) FROM states').fetchone()
        self.assertEqual(count[0],2)

    def test_2_get_active(self):
        test = StateModel.get_current_state()
        self.assertEqual(test.name,self.state1.name)

    def test_3_get_by_id(self):
        test = StateModel.get_state_by_id(2)
        self.assertEqual(test.name,self.state2.name)

    def test_4_update(self):
        self.state1.is_active=False
        self.state1.update()
        self.state2.is_active=True
        self.state2.update()
        test = StateModel.get_current_state()
        self.assertEqual(test.name,self.state2.name)


if __name__ == '__main__':
    unittest.main()