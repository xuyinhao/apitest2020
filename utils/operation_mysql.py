import pymysql
# bit类型 转换
from pymysql import converters

converions = converters.conversions
converions[pymysql.FIELD_TYPE.BIT] = lambda x: '0' if '\x00' else '1'


class OperationMysql():

    def __init__(self,host=None,port=None,user=None,password=None,database=None):
        self.host = host if host else "127.0.0.1"
        self.port = port if port else 3306
        self.user = user if user else "remote"
        self.password = password if password else  "hhrhl2016"
        self.database = database if database else "aiodb"
        self.charset = "utf8"

    #连接数据库，获得游标
    def connectdb(self):
        #host=None, user=None, password="", database=None, port=0,
        print(self.host,self.port,self.user,self.password,self.database)
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password = self.password,
                charset = self.charset,
                database = self.database )
        except Exception as e:
            print("Connect error :" , e)
            return False

        self.cur = self.conn.cursor()
        return True
    #关闭游标和数据库连接
    def closedb(self):
        self.cur.close()
        self.conn.close()

    #执行数据库，insert,delete,updata等（不包含select)
    def exec_mysql(self, sql):
        try:
            if self.connectdb():
                self.cur.execute(sql)
                self.conn.commit()
            else:
                return "Error:execute error："+str(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            try:
                self.closedb()
            except:
                pass

    #查询并返回，
    def _get_one_or_more(self,sql,oneorall):
        try:
            if self.connectdb():
                self.cur.execute(sql)
                self.conn.commit()
            else:
                return "Error:Select error："+str(sql)
            if oneorall == "one":
                get_all = self.cur.fetchone()
            else:
                get_all = self.cur.fetchall()
            return get_all
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            try:
                self.closedb()
            except Exception as  e:
                pass

    #查询并返回所有信息
    def select_get_all(self, sql):
        return self._get_one_or_more(sql, "all")

    #查询并返回一个信息
    def select_get_one(self,sql):
        return self._get_one_or_more(sql,"one")

if __name__ == '__main__':
    m = OperationMysql(host='127.0.0.1',port=3306)
    res = m.select_get_all("select ips,(monitor+0) from nodes;")
    res2 = m.select_get_one("select ips,(monitor+0) from nodes;")
    print(res,'\n',res2)
