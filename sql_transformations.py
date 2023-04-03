import array
import decimal
from decimal import Decimal
from codecs import charmap_build
from unicodedata import decimal
import mysql.connector as mysql
import statistics



def connect_source():
    print("Connecting Source")
    try:
        conn = mysql.connect(
        host= 'localhost',
        user='root',
        password='root123',
        db='classicmodels'    
    )
        print("Source connected.")
        return conn
    except:
        print("Connection not established.")



def attribute_index(attribute,table_list):
    counter = 0
    for x in table_list:
        # print(x[0])
        if attribute == x[0]:
            return counter
        else:
            counter = counter + 1



def table_list_func(tables):
    table_list = []
    for x in tables:
        # print(x[0])
        table_list.append(x[0])
    return table_list



def sql_result(cursor, table, attribute):
    print("sql_result func entered.")
    sql = "select " + attribute + " from " + table + ";"
    cursor.execute(sql)
    results = cursor.fetchall()
    array_list = []
    for x in results:
        array_list.append(x[0])
    return array_list

def datatype_check(x,attribute):
    if isinstance(x,(int,float,Decimal)):
        print("Attribute selected is an integer as expected.")
        return 0
    else:
        print("Arithmatic Operations unapplicable on selected attribute("+attribute+") due to incorrect datatype.")
        return 1


def arithmatic_operation_function(array_list,arithmatic_operation):
    if arithmatic_operation == "MEAN":
        return statistics.mean(array_list)
    elif arithmatic_operation == "MODE":
        return statistics.mode(array_list)
    elif arithmatic_operation == "MEDIAN":
        return statistics.median(array_list)


def sql_trans(attribute = "orderLineNumber",arithmatic_operation = "MEAN"):
    conn = connect_source()
    cursor = conn.cursor()
    cursor.execute("select database();")
    database = cursor.fetchone()
    cursor.execute("show tables;")
    tables = cursor.fetchall()
    table_list = table_list_func(tables)

    table = "orderdetails"
    cursor.execute("describe " + table)
    table_desc = cursor.fetchall()
    array_list = sql_result(cursor, table, attribute)
    bool = datatype_check(array_list[0],attribute)
    if bool == 0:
            arithmatic_result = arithmatic_operation_function(array_list,arithmatic_operation)
            print ("Result of "+ arithmatic_operation + ": ", arithmatic_result)

    elif bool == 1:
            print("Selected Operation("+ arithmatic_operation +") failed.")
            # wrong type of column selected for Arithmatic operations
   
    

if __name__=="__main__":
    sql_trans()