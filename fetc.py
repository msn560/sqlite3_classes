class fetc:
    tableName, isWHERE, whereStr, wANDor = "", {}, "",[]
    fetc_default_str ="SELECT * FROM {}"
    def __init__(self,db) -> None:
        self.db = db
        pass
    def setTable(self,t):
        if isinstance(t,str):
            self.tableName=t
        else:
            raise("fetc||setTable : tableName is str")
        return self
    def getOne(self):
        return self.getALL(count=1)
    def getALL(self,count=0):
        if len(self.tableName) < 1:
            raise("fetc||getALL : Table name empty")
        self.db.im.execute(self.toStr()) 
        if count == 0:
            rData =  list(self.db.im.fetchall())
        else:
            rData= list(self.db.im.fetchmany(count))
        if len(rData) >0:
            tableInfo = dict(self.db.info().getAllTablesInfo())
            returnData = []
            for d in rData:
                newData = { }
                i=0
                for k in tableInfo[self.tableName]:
                    newData[k]=d[i]
                    i +=1
                returnData.append(newData)
            return returnData
        return  [ ]

    def addWhere(self,wkey,wval,wANDor="and"):
        if len(self.tableName)<1:
            raise("fetc||addWhere : Table name empty")
        tableInfo = dict(self.db.info().getAllTablesInfo())
        if not wkey in tableInfo[self.tableName]:
            raise("fetc||addWhere : key is not in table")
        self.isWHERE[wkey]=wval
        self.wANDor.append(wANDor)
        return self 
    def setWhereStr(self, whereStr):
        self.whereStr = whereStr
        return self
    def toStr(self):
        fe = self.fetc_default_str.format(self.tableName)
        if len(self.whereStr)>0:
            fe += " "+self.whereStr
        elif len(self.isWHERE.keys()) > 0:
            ii = 0
            fe += " WHERE  "
            for kk in self.isWHERE.keys():
                fe += "{} = '{}' ".format(kk, self.isWHERE[kk])
                if len(self.wANDor) > (ii+1):
                    fe += " {} ".format(self.wANDor[ii])
                ii += 1
        return fe