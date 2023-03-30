from DB import sql

ss = sql()
#
#ss.createTable()
#ss.tablesController()

#print("getAllTablesInfo:",ss.getAllTablesInfo())
create = ss.create()
#sstr = create.name("user").addIDKey(True).addKey( "username").addKey("mail").addKey("pass").toStr().toDict()

#print(sstr.tableSql_str)
#print(sstr.tableSql_dict)
d = {
        'user': 
                [
                    "id",
                    'name',
                    'username',
                    'password',
                    'mail',
                    'check_mail',
                    'rutbe',
                ],
        'login_log': 
                [
                    "id",
                    'userId',
                    'start',
                    'finish',
                    'status', 
                ],
    }
 
sql().create().doTable(userTables=d)
val = sql().insert().setTable("user").addValues(["muhammed","unkowUser","pasWord#","example@gmail.com","1","1"])
print(val.save()) 
f = sql().get().setTable("user").addWhere(
    "username", "unkowUser").addWhere("password", "pasWord#")
print("f.toStr: ", f.toStr())
print(f.getALL()[0])
#{'id': 1, 'name': 'muhammed', 'username': 'unkowUser', 'password': 'pasWord', 'mail': 'example@gmail.com', 'check_mail': '1', 'rutbe': '1'}

