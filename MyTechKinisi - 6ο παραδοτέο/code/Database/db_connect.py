import mysql.connector
import mysql
import time

class database():
    def __init__(self):
        self.isConnect = False
        self.dbHost = 'localhost'
        self.dbName = 'app_db-1'
        self.dbUser = 'root'
        self.dbPass = ''


    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.dbHost, database=self.dbName, user=self.dbUser,password=self.dbPass)
            if self.connection.is_connected():
                self.isConnect = True
        except:
            self.isConnect = False

    def close(self):
        self.connection.close()

    def checkConnection(self):
        return self.isConnect

    def query(self, query):
        if (self.isConnect is False):
            self.connect()
        cursor = self.connection.cursor()
        self.connection.commit()
        cursor.execute(query)
        records = cursor.fetchone()
        return records[0]

    def query_all(self, query):
        if (self.isConnect is False):
            self.connect()
        cursor = self.connection.cursor()
        self.connection.commit()
        cursor.execute(query)
        records = cursor.fetchall()
        return records[0]

    def query_all_d(self, query):
        if (self.isConnect is False):
            self.connect()
        cursor = self.connection.cursor()
        self.connection.commit()
        cursor.execute(query)
        records = cursor.fetchall()
        return records

if __name__=='__main__':
    db=database()
    print(db.isConnect)