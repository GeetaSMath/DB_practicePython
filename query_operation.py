import logging
import mysql.connector as connector
from db_connectionpython import DataBase

logging.basicConfig(filename='employee_service.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')

class DBQueries:
    def __init__(self):
        self.connection = DataBase.mysqlconnect_database()
        self.cursor = self.connection.cursor(buffered=True)

    def insert_data(self, id, name, salary, startDate):
        """
         created insert_data function to insert data and pass parameters
        :param id: passed param id
        :param name: passed param name
        :param salary: passed salary
        :param startDate: passed startDate to pass
        :return: insert user data
        """
        try:
            query1 = "insert into payroll_service(id, name, salary, startDate) values(%d ,'%s',%f, '%s')" \
                             % (id, name, salary, startDate)
            self.cursor.execute(query1)
            self.connection.commit()
            logging.info("Suceefully Get All the Employee services")
            logging.debug("Employee Detailes are")
            return "Inserted data Successfully"
        except Exception as err:
                logging.error(f"Error: {err}")

    def retrive_data(self):
        """
         created function to retrive data
        :return:
        """
        try:
            query3 = 'select * from payroll_service'
            self.cursor.execute(query3)
            self.connection.commit()
            logging.info("Retrive data which inserted")
            logging.debug("existed data")
            res = self.cursor.fetchall()
            for val in res:
                print(val)
        except Exception as err:
                logging.error(f"Error: {err}")

    def update_data(self, name, id):
        """
        created updaate function
        :param name: param passed name
        :param id: param paased id
        :return:
        """
        query4 ="update payroll_service set name='%s' where id=%d" %(name, id)
        self.cursor.execute(query4)
        self.connection.commit()

    def delete_data(self, id):
        """
        created delete_data function
        :param id:passed id reference to delete data
        :return:
        """
        query5 = "delete from payroll_service where id=%d" % id
        self.cursor.execute(query5)
        self.connection.commit()

    def insert_employee_data(self, id, name, location, salary):
        """
        created insert employee_data function pass param
        :param id: id passed as param
        :param name: name of the employee as param
        :param location: location of the employee as param
        :param salary: salary of the employee as param
        :return: it will insert data
        """
        query1 = "insert into employee_data(id, name, location, salary) values(%d ,'%s','%s', %f)" \
                 % (id, name, location, salary)
        self.cursor.execute(query1)
        self.connection.commit()
        return "Inserted data Successfully"



store_data = DBQueries()
# store_data.payroll_service()
store_data.insert_data(1221, 'pavan', 2000.00, "2020-02-02")
store_data.retrive_data()
#store_data.insert_employee_data()

