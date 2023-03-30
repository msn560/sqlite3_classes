class insert:
    tableName, values= None,[]
    insert_default_str = """INSERT INTO {} VALUES ({})"""
    def __init__(self,db) -> None:
        self.db = db 
        pass
    def setTable(self,tableName):
        self.tableName = tableName
        return self
    def addValues(self,v=[]):
        if isinstance(v,list):
            self.values = v
        else:
            raise ("insert|| addValues : values =[]")
        return self
    def save(self):
        self.db.im.execute(self.toStr())
        last_id = self.db.im.lastrowid
        self.db.vt.commit() 
        tableInfo = dict(self.db.info().getAllTablesInfo())
        returnData = { }
        i_val =  self.db.im.execute("""SELECT * FROM {} WHERE id='{}' """.format(self.tableName, last_id)).fetchone()
        ii = 0
        for vk in tableInfo[self.tableName]:
            returnData[vk] = i_val[ii]
            ii +=1
        return returnData

    def toStr(self):
        if self.tableName is None:
            raise("insert||toStr : tableName is exits")
        if len(self.values)<1:
            raise("insert||toStr : values is empty")
        tableInfo = dict(self.db.info().getAllTablesInfo())
        if not self.tableName in tableInfo.keys():
            raise("insert||toStr : {} table is not found!".format(self.tableName))
        if tableInfo[self.tableName][0] == "id":
            insert_str = "NULL,"
        else:
            insert_str = ""
        ii = 1
        for v in self.values:
            insert_str+= '"'+v+'"'
            if len(self.values)>ii:
                insert_str +=","
            ii += 1
        return self.insert_default_str.format(self.tableName,insert_str)
