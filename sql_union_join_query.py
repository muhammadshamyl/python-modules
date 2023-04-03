from contextlib import nullcontext
import mysql.connector as mysql


def connect_source(database = 'classicmodels'):
    print("Connecting Source")
    try:
        conn = mysql.connect(
        host= 'localhost',
        user='root',
        password='root123',
        db= database    
    )
        print("Source connected.")
        return conn
    except:
        print("Connection not established.")

def sql_union(cursor,table,table2,colT1,colT2,where1,where2,orderby):
    query = ""
    if where1 == "":
        print("null where condition entered")
        query = "SELECT " + colT1 + " FROM " + table + " UNION " + "SELECT " + colT2 + " FROM " + table2 + " ;"
        print("query: ", query)
    
    elif where1 != "":
        print("where condition entered")
        query = "SELECT " + colT1 + " FROM " + table + " WHERE " + where1 + " UNION ALL " + "SELECT " + colT2 + " FROM " + table2 + " WHERE " + where2 
        

    if orderby != "":
        print("orderby condition entered.")
        query = query + " ORDER BY " + orderby
    elif orderby == "":
        print ("orderby deemed empty")
    query = query +" ;"
    print("query: ", query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)    

def sql_join(cursor,colT1,table,table2,JOIN,ON):
    query = "SELECT " + colT1 + " FROM " + table + " " + JOIN + " " + table2 + " ON " + ON +";"
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result) 

def query_main(table = "orders", sql_operation = "JOIN",JOIN = "INNER JOIN",ON = "orders.orderNumber = orderdetails.orderNumber", table2 = "orderdetails",colT1 = "orders.orderNumber",colT2 = "*",where1 = "orderNumber = 10100",where2 = "orderNumber = 10100",orderby = "orderNumber"):
    conn = connect_source()
    cursor = conn.cursor()
    cursor.execute("select database();")
    database = cursor.fetchone()
    cursor.execute("show tables;")
    tables = cursor.fetchall()
    print(tables)
    if sql_operation == "UNION":
        sql_union(cursor,table,table2,colT1,colT2,where1,where2,orderby)
    elif sql_operation == "JOIN":
        sql_join(cursor,colT1,table,table2,JOIN,ON)

if __name__=="__main__":
    query_main()