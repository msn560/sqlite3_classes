
class createTable:
    tableName,isAddID, tableKey = "",False,[]
    isImportant = False
    tableSql_str ,tableSql_dict= "",{}
    createTable_default_str = """CREATE TABLE IF NOT EXISTS {} ({}{})"""
    def __init__(self,db) -> None:
        self.db = db
        pass
    def clear(self):
        self.tableKey = []
        return   self

    def doTable(self, userTables, important=False):
        str_tables = self.clear().dictToStr(userTables)
        
        if len(str_tables) < 1:
            raise("sql.doTable ||  Table to insert not found")
        if important:
            for tname in userTables.keys():
                self.im.execute(""" DROP TABLE {}; """.format(tname))
        for s in str_tables:
            self.db.im.execute(str(s))
        return self
    def dictToStr(self,tableData ):
        str__ =[]
        if isinstance(tableData,dict):
            for k in tableData.keys():
                new_class = self.clear()
                for kk in tableData[k]:
                    if kk =="id":
                        new_class = new_class.name(k).addIDKey(True)
                    else:
                        new_class = new_class.name(k).addKey(kk)
                str__.append(new_class.toStr())
             
        else:
            raise("createTable.dictToStr ||  Table data is not dict. eg: {'tablename':['tableVal1','tableVal2','tableVal3']}")
        return str__
    def name(self,n):
        if isinstance(n,str):
            self.tableName = n
        else:
            raise("Table name String")
        return self
    def addKey(self,k):
        if isinstance(k,str):
            self.tableKey.append(k)
        elif isinstance(k,list):
            self.tableKey = k 
        else: 
            raise( "Table keys String or List")
        return self
    def setKeys(self,key):
        self.tableKey = key
        return self
    def addIDKey(self,status = True):
        self.isAddID = status
        return self
    def setImportant(self,s =True):
        if isinstance(s,bool):
            self.isImportant = s
        else:
            raise("True & False")
        return self
    def toDict(self):
        d = {}
        if self.isAddID:
            d[self.tableName] = ["id"]+self.tableKey
        else:
            d[self.tableName] = self.tableKey
        self.tableSql_dict = d
        return self
    def toStr(self):
        new_str = self.createTable_default_str
        if len(self.tableName)<1:
            raise("table name is missing")
        elif isinstance(self.tableKey,list):
            if len(self.tableKey)<1:
                raise("Table keys ​​are missing")
            else: 
                add_Id_str = "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                if not self.isAddID:
                    add_Id_str = ""

                return new_str.format(self.tableName,add_Id_str,str(",".join(self.tableKey))) 
        else:
            raise("Table keys ​​are missing or no list")

# EG : 
# ss = sql()
#
#ss.createTable()
#ss.tablesController()


#print("getAllTablesInfo:",ss.getAllTablesInfo())
#create = ss.create
#sstr = create.name("user").addKey("username").addKey("mail").addKey("pass").toStr() 
#print(sstr)
