
#create database
class DB():
    DB_NAME='mysql'

    TABLE = {}
    TABLE['AdminUsers'] = (
        "CREATE TABLE `AdminUsers` ("
        "  `user_no` int(1) NOT NULL AUTO_INCREMENT,"
        "  `emailad` varchar(90),"
        "  `uname` varchar(50),"
        "  `new_pin` char(4),"
        "  `old_pin` char(4),"
        "  PRIMARY KEY (`user_no`))")

    cnx = mysql.connector.connect(user='root',
                                    password='baylon06',
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

    #insert data from user
    user_no = cursor.lastrowid
    data_email = input("Enter your email address: ")
    data_uname = input("Username: ")
    data_newpin = input("PIN: ")
    result=''
    for i in range(0, len(data_newpin)):
                result = result + chr(ord(data_newpin[i]) - 2)
    cursor.execute("""
        INSERT INTO AdminUsers
        (user_no, emailad, uname, new_pin) VALUES
        (%s, %s, %s, %s)""" , (user_no, data_email, data_uname, result))

    cnx.commit()

    #query
    query = "SELECT user_no, emailad, uname, new_pin FROM AdminUsers"

    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        #user_no = row[0]
        #emailad = row[1]
        #uname = row[2]
        #new_pin = row[3]
    #print ("User No. = %s, Email Address = %s, Username = %s, Pin = %s" % \
              #(user_no, emailad, uname, new_pin))
        print (row)

    #update
    query = "UPDATE AdminUsers SET old_pin = new_pin"
    try:
       # Execute the SQL command
       cursor.execute(query)
       # Commit your changes in the database
       cnx.commit()
    except:
       # Rollback in case there is any error
       cnx.rollback()

    cursor.close()
    cnx.close()
DB()