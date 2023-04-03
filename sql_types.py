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


def table_list_func(tables):
    table_list = []
    for x in tables:
        # print(x[0])
        table_list.append(x[0])
    return table_list


def attribute_index(attribute,table_list):
    counter = 0
    for x in table_list:
        # print(x[0])
        if attribute == x[0]:
            return counter
        else:
            counter = counter + 1


def sql_trans(attribute = "orderNumber",arithmatic_operation = "MEAN"):
    conn = connect_source()
    cursor = conn.cursor()
    cursor.execute("select database();")
    database = cursor.fetchone()
    cursor.execute("show tables;")
    tables = cursor.fetchall()
    table_list = table_list_func(tables)
    # table = table_list[0]
    table = "customers"
    cursor.execute("describe " + table)
    table_desc = cursor.fetchall()
    for x in table_desc:
        print (x)
    print("-----------------------------------------------------------")
    x = table_desc[-1][1]
    print (type(x))
    index = attribute_index(attribute,table_desc)


if __name__=="__main__":
    sql_trans()