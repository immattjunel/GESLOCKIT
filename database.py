import mysql.connector
from mysql.connector import errorcode

DB_NAME='mysql'

TABLE = {}
TABLE['AdminUsers'] = (
    "CREATE TABLE `AdminUsers` ("
    "  `user_no` int(1) NOT NULL AUTO_INCREMENT,"
    "  `emailad` varchar(90),"
    "  `uname` varchar(50),"
    "  `new_pin` int(4),"
    "  `old_pin` int(4),"
    "  PRIMARY KEY (`user_no`))")

cnx = mysql.connector.connect(user='root',
                                password='parasathesis',
                                host='localhost',
                                database='mysql')
cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = DB_NAME    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLE.items():
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()
