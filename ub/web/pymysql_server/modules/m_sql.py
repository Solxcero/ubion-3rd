import pymysql
import imp
imp.reload

class Database():
    def __init__(self):
        self._db = pymysql.connect(
        user = 'root',
        password = '0789',
        host = 'localhost',
        db = 'ubion',
        charset = 'utf8'    
        )

        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def execute(self,_sql, _values={}):       
        self.cursor.execute(_sql, _values)

    def executeAll(self, _sql, _values={}):       
        self.cursor.execute(_sql, _values)
        self.result = self.cursor.fetchall()
        return self.result

    def commit(self):
        self._db.commit()


