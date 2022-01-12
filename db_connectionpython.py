import mysql.connector
from mysql.connector import errorcode

def mysqlconnect_database():
    # To connect MySQL database
    try:
        conn = mysql.connector.connect(host='127.0.0.1', user='root', port='3306', password='Geeta@123',
                                       database=' payroll_employeeservice')
        # created object to call conn object
        cursor = conn.cursor()
           # data insert into table
           # inserted value by using list so ,can insert data and to reduce code redundancy
        query1 = 'insert into payroll_service values(%s ,%s, %s, %s)'
        query2_insertdata = [(111, 'anwitha', 120000, "2012-02-02"), (112, 'geeta', 25000, "2014-02-04"), (113, "aishu", 30000, "2015-02-02")]
        cursor.executemany(query1,query2_insertdata,)


           # read operation ->to read data from existed table
           # used fetchall() method it will store all data into res object
        query3 = 'select * from payroll_service'
        cursor.execute(query3)
        res = cursor.fetchall()
        for val in res:
            print(val)
   # Update operation
        query4 = 'select * from payroll_service set name=anu where id=111'
        cursor.execute(query4)
    # delete operation
        query5 = 'delete from payroll_service where name="geeta"'
        cursor.execute(query5)
        conn.commit()
    except mysql.connector.Error  as  er:
        if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("invalid username or password")
        elif er.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")

        else:
            print(er)
    finally:
        conn.close()
        return conn

call = mysqlconnect_database()
print(call)

