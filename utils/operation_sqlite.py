import sqlite3

file = "../data/apidb202004.db"

class OperationSqlite3():
    def __init__(self,dbfilename=None):
        self.db = file
        if dbfilename:
            self.db = dbfilename

    def connectdb(self):
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()
    def closedb(self):
        self.cur.close()
        self.conn.close()

    def exec_sqlite3(self,sql):
        try:
            self.connectdb()
            result_sql = self.cur.execute(sql)
            self.conn.commit()
            print(result_sql.fetchall())
        except Exception as  e:
            print(e)
            self.conn.rollback()
        finally:
            self.closedb()

if __name__ == '__main__':
    s3 = OperationSqlite3()
    s3.exec_sqlite3('insert into login values (11,"aaa")')
    s3.exec_sqlite3('select * from login;')


    # m=sqlite3.connect(file)
    # m.cursor()
    # # m.execute('CREATE TABLE IF NOT EXISTS  login(id int,name string);')
    # m.execute('INSERT INTO login values (2,"b")')
    # m.execute('INSERT INTO login values (1,"a")')
    # m.commit()
    # a = m.execute('select * from login;')
    #
    # print(a.fetchall())
    # m.close()