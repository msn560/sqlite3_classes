import sqlite3 as db
from json import dumps
from Create import createTable
from Info import info
from insert import insert
from fetc import fetc

class sql: 
    def __init__(self,dbFile="data.db") -> None:
        self.vt = db.connect(dbFile)
        self.im = self.vt.cursor() 
        self.DBtables = self.info().getAllTablesInfo()
        self.userTables = self.DBtables 

    def create(self):
        return createTable(self)
    def info(self):
        return info(self)
    def insert(self):
        return insert(self)
    def get(self):
        return fetc(self)
    
    