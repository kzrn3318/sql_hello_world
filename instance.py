import sqlite3
class ret_from_db():
    def __init__(self,db):
        self.db = db

    #カラム指定で取り出す
    def ret_column(self,table,column=""):
        assert bool(column), "no column is spcified"
        conn= sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("select {} from {}".format(column,table))
        val = cur.fetchall()
        cur.close()
        conn.close()
        return val

    #すべて取り出すl
    def ret_all(self,table):
        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute("select * from {}".format(table))
        val = cur.fetchall()
        cur.close()
        conn.close()
        return val