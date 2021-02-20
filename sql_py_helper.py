import mysql.connector
from mysql.connector import Error
from copy import deepcopy


class SqlConnection:
    def __init__(self, host="localhost", database="FAKE_AMAZON", user="root", password="mysqluah"):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 database='FAKE_AMAZON',
                                                 user='root',
                                                 password='mysqluah')
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                self.cursor = self.connection.cursor()
                self.cursor.execute("select database();")
                record = self.cursor.fetchone()
                print("You're connected to database: ", record)
        except Error as e:
            print("Error while connecting to MySQL", e)


    def __del__(self):
        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
        else:
            print("Connection already closed")


    def close(self):
        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
        else:
            print("Connection already closed")


    def sql_command(self, command):
        self.cursor.execute(command)
        return self.cursor
