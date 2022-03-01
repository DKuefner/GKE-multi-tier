"""
Simple Python App to demonstrate delpoyment using GKE
This app will run in one container and will connect
with MySQL database running as another container using service name
"""

from flask import Flask, request
app = Flask(__name__)
import mysql.connector
from mysql.connector import errorcode

def get_db_conn(host, user, passwd, db):
    """
    Get connection to MySQL database
    """
    print ("vor connect")
    try:
        connection = mysql.connector.connect(host=host,
                database=db,
                user=user,
                password=passwd,auth_plugin='mysql_native_password')
        if connection.is_connected():
            db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    except Error as e:
        print("Error while connecting to MySQL", e)

def db_init(host, user, passwd, db):
    """
    Initialize the database by creating employee table
    """
    try:
        connection = mysql.connector.connect(host=host,
                database=db,
                user=user,
                password=passwd,auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        # create table
        # cursor.execute('drop table if exists employee')
        cursor.execute('''create table if not exists employee(id int, name varchar(20))''')
        cursor.close()
        connection.commit()
    except Exception as msg:
        print("Exception while initializing database : ", msg)


@app.route('/')
def greet():
    """
    Greet to visitors of url http://IP:5000/
    """

    return 'Greetings from GCP Team2! \n'


@app.route("/storedata", methods=["POST"])
def store_data():
    """
    Store the employee data in database and return msg
    """
    msg=''
    try:
        print("Now inserting into table")
        connection = mysql.connector.connect(host="localhost",
                database="Electronics",
                user="root",
                password="admin",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("insert into employee values (%s, '%s')"%(request.form['id'], request.form['name']))
        connection.commit()
        msg = "Inserted data for Employee\n "
        print("Inserted Data for Employee: ", request.form['name'])
    except Exception as msg:
        print( "Exception : %s")%(msg)
        msg = "Exception while inserting data %s"%(msg)
    return msg 


@app.route("/getdata/<int:id>", methods=["GET"])
def get_data(id):
    """
    Get Employee data using Employee ID
    """
    msg=''
    select = "select * from employee where id=%d" %(id)
    try:
        connection = mysql.connector.connect(host="localhost",
                database="Electronics",
                user="root",
                password="admin",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute(select)
        res = cursor.fetchone()
        msg = "Employee Details ID : %d  Name : %s"%(res[0], res[1])
    except Exception as msg:
        print("Exception : ", msg)
    return msg


if __name__ == '__main__':
    db_init(host="mysql-service.default", user="root", passwd="admin", db="Electronics")
    app.run(host="0.0.0.0", port=5000)
