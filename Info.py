
class info:
    def __init__(self,db) -> None:
        self.db = db
        pass

    def getAllTablesInfo(self, db=None):
        if db is None:
            db = self.db 
        data = {}
        for t in self.tableNames(db):
            data[t] = self.tableKeys(t,db)
        return data
    def tableNames(self,db=None):
        if db is None:
            db = self.db
        result = db.im.execute( "SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        if len(result) == 0:
            return []
        else:
            return sorted(list(zip(*result))[0])
    def tableKeys(self,table=None,db=None):
        if db is None:
            db = self.db
        if table is None:
            table = self.tableNames(db)
        if isinstance(table,str):
            result = db.im.execute("PRAGMA table_info('%s')" % table).fetchall()
            return list(zip(*result))[1]
        elif isinstance(table,list) or isinstance(table,tuple):
            r = []
            for t in table:
                result = db.im.execute("PRAGMA table_info('%s')" % t).fetchall()
                r.append(list(zip(*result))[1])
            return r
        else:
            raise("tableKeys Error: table is str,list,tuple")
        
