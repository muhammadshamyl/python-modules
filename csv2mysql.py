from asyncore import loop
from contextlib import nullcontext
# from sqlite3 import connect
import re, json
from warnings import catch_warnings
import mysql.connector as mysql
import decimal


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
    
    conn.close()
    
def connect_destination():
    try:
        conn = mysql.connect(
        host= 'localhost',
        user='root',
        password='root123',
        db='classic_replica'
        )
        print("Destination connected.")
        return conn

    except:
        print("Destination connection failed to be established")

def pipeline_connection():
    try:
        conn = mysql.connect(
        host= 'localhost',
        user='root',
        password='root123',
        db='pipeline_database'
        )
        print("Pipeline database connected.")
        return conn

    except:
        print("Pipeline connection failed to be established")

# check if the table you're replicating pre-exists in the data warehouse.
def check_table(cursor_destination, table_name):
    cursor_destination.execute("show tables;")
    table_info = cursor_destination.fetchall()
    table_check_bool = 0
    for x in table_info:
        print("Table info: ", x[0])
        if table_name == x:
            print ("Table pre-exists.")
            table_check_bool = 0
        elif table_name != x:
            table_check_bool = 1
            print ("Table does not exist.")
    return table_check_bool  

def create_query_construct(column_name, column_datatype, column_null,prim_key_index,table_name):
    column_count = len(column_name)
    string_query = ""
    for x in range(len(column_name)):
        string_query = string_query + column_name[x] + " " + column_datatype[x] + " " + column_null[x] + ","
        if x == column_count - 1:
            string_query = string_query + "PRIMARY KEY(" + column_name[prim_key_index] + "));"
    
    string_query = "CREATE TABLE " + table_name + "(" + string_query
    print ("string_query: " + string_query)
    return string_query


def insert_query_construct(column_name, table_name):
    insert_query = "INSERT INTO " + table_name + " ("
    print("column length: ", int(len(column_name)))
    # see if there is a smarter way without loop_counter
    loop_counter = 0
    print("length", len(column_name))
    for x in column_name:
        insert_query = insert_query + x
        if loop_counter < len(column_name) - 1:
            insert_query = insert_query + ','

        loop_counter = loop_counter + 1

    insert_query = insert_query + ") VALUES ("
    loop_counter = 0
    # to construct (%s,%s,) part of query
    for x in column_name:
        insert_query = insert_query + "%s"
        if loop_counter < (len(column_name)) - 1:
            insert_query = insert_query + ","
        if loop_counter == (len(column_name)) - 1:
            insert_query = insert_query + ")"

        loop_counter = loop_counter + 1

    # insert_query = insert_query + '"'
    print("Insert query:", insert_query)
    return insert_query


def fetch_and_insert(cursor_source,cursor_destination,column_name,table_name,conn2,source_database,destination_database,table_name_dest,connection_type,pipeline_type,column_datatype):
    cursor_source.execute("select * from " + table_name)
    data = cursor_source.fetchall()
    insert_query = insert_query_construct(column_name,table_name)
    # currently gives error because primary key is repeating due to repetitive data 
    # should a check be added? That would mean traversal of destination db as well
    for x in data:
        cursor_destination.execute(insert_query,x)
   
    # conn2.commit()
    conn_pip = pipeline_connection()
    # condition to check if ID of pipeline does not previously exist, add it into pipeline table (needs to be implemented)
    # else proceed to populate cycles_log table
    
    print("No of Rows: ", len(data))
    row_count = len(data)
    print(data[-1])
    last_row = data[-1]
    pipeline_database_func(source_database,destination_database,conn_pip, table_name,table_name_dest,connection_type,pipeline_type,last_row,column_name,column_datatype,row_count)

def pipeline_database_func(source_database,destination_database,conn_pip, table_name, table_name_dest, connection_type, pipeline_type,last_row,column_name,column_datatype,row_count):
    cursor_pipeline = conn_pip.cursor()
    cursor_pipeline.execute("select * from pipeline_profile")
    profile_query = cursor_pipeline.fetchall()
    if len(profile_query) == 0:
        pipeline_first_insert(conn_pip,cursor_pipeline,table_name, table_name_dest, connection_type, pipeline_type,source_database,destination_database)
        print("Entering pipeline_first_insert")
    else:
        pipeline_update(conn_pip,source_database,destination_database,table_name, table_name_dest,connection_type, pipeline_type,last_row,column_name,column_datatype,row_count)
        print("Entering pipeline_profile_update")
        # pipeline_log_update()


def pipeline_update(conn_pip,source_database,destination_database,table_name, table_name_dest,connection_type, pipeline_type,last_row,column_name,column_datatype,row_count):
    pipeline_cursor = conn_pip.cursor()
    pipeline_cursor.execute("select * from pipeline_profile")
    pipeline_rows = pipeline_cursor.fetchall()
    for x in pipeline_rows:
        if x[6] == source_database and x[7] ==  destination_database and x[1] == table_name and x[2] == table_name_dest:
            id = x[0]
            cycle = x[5]
            pipeline_profile_update(pipeline_cursor,id,cycle)
            pipeline_log_update(pipeline_cursor,column_name,column_datatype,last_row,row_count,id)
            conn_pip.commit()
        # else:
            # you have to add a new profile and then add log into pipeline_log
def pipeline_first_insert(conn_pip,cursor_pipeline,source_table, destination_table, connection_type, pipeline_type,source_database,destination_database):
    id = 1
    cycles = 1
    
    insertion_query = """INSERT INTO pipeline_profile(id,source_table,destination_table,connection_type,pipeline_type,cycles,source_database,destination_database) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    record = (id,source_table, destination_table, connection_type, pipeline_type,cycles,source_database,destination_database)
    print("Insertion query: ", insertion_query)
    try:
        cursor_pipeline.execute(insertion_query,record)
        conn_pip.commit()
        print("pipeline profile query executed")
    except (mysql.Error, mysql.Warning) as e:
        print(e)
    # INSERT INTO pipeline_profile(id,source_table,destination_table,connection_type,pipeline_type,cycles) VALUES(1, 'customers', 'customers', 'mysql-mysql', 'ETL', 1)            
def pipeline_profile_update(pipeline_cursor,id, cycle):
    cycle = int(cycle) + 1
    cycle_query = "update pipeline_profile set cycles = %s where id = %s"
    record = (cycle,id)
    try:
        pipeline_cursor.execute(cycle_query,record)
        print("pipeline cycle query executed")
    except (mysql.Error, mysql.Warning) as e:
        print(e)

def pipeline_log_update(pipeline_cursor,column_name,column_datatype,last_row,row_count,id):
    columns_name = str(column_name)
    columns_type = str(column_datatype)
    row = []
    for l in last_row:
        if isinstance(l, decimal.Decimal):
            row.append(float(l))
        else:
            row.append(l)
    print("ID", id)
    print("names: ", columns_name)
    print("_____________________________________________________________________________________________________________________")
    print("last row", row)
    print("_____________________________________________________________________________________________________________________")
    print("Columns Type", columns_type)
    print("_____________________________________________________________________________________________________________________")
    print("row count: ", row_count)
    print("_____________________________________________________________________________________________________________________")
    final_row = ', '.join(str(r) for r in row)
    row_to_insert = (id, columns_name, final_row, "nullcontext","nullcontext","nullcontext",0.10,columns_type,row_count)
    query = "insert into pipeline_logs(id,source_schema,last_log,start_time,end_time,execution_period,volume_transferred,schema_datatype,rows_added) values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    print("row to insert: ", row_to_insert)
    print(query)
    pipeline_cursor.execute(query, tuple(row_to_insert))
    pipeline_cursor.execute("select * from pipeline_logs")
    result = pipeline_cursor.fetchall()
    last_row_compare(row,last_row)
def last_row_compare(row,last_row):
    for x in row:
        print(x)
    print("______________________________________________________________________________________________________________________")
    for x in last_row:
        print(x)

    a = set(row)
    b = set(last_row)
    if a == b:
        print("both are equal")
    else:
        print("Not equal")
def server_version(source_server_info,destination_server_info,pipeline_server_info):
    print("Connected to Source MySQL Server version ", source_server_info)
    print("Connected to Destination MySQL Server version ", destination_server_info)
    print("Connected to Pipeline MySQL Server version ", pipeline_server_info)

def database_connected(source_database, destination_database, pipeline_database):
    print("You're connected to source database: ", source_database)
    print("You're connected to destination database: ", destination_database)
    print("You're connected to destination database: ", pipeline_database)

def connection():
    connection_type = "mysql-mysql"
    pipeline_type = "ETL"
    conn = connect_source()
    conn2 = connect_destination()
    conn_pip = pipeline_connection()
    source_server_info = conn.get_server_info()
    destination_server_info = conn.get_server_info()
    pipeline_server_info = conn.get_server_info()
    server_version(source_server_info,destination_server_info,pipeline_server_info)
    cursor_source = conn.cursor()
    cursor_destination = conn2.cursor()
    cursor_pipeline = conn_pip.cursor()
    cursor_source.execute("select database();")
    cursor_destination.execute("select database();")
    cursor_pipeline.execute("select database();")
    source_database = cursor_source.fetchone()
    source_database = source_database[0]
    destination_database = cursor_destination.fetchone()
    destination_database = destination_database[0]
    pipeline_database = cursor_pipeline.fetchone()
    database_connected(source_database, destination_database, pipeline_database)
    table_name = "customers"
    table_name_dest = table_name    #this will be later set to be retrieved from frontend. Or it will be automatically assigned
    
    cursor_source.execute("DESCRIBE " + table_name)
    columns = cursor_source.fetchall()
       
    # loop SHOWS HOW TO TRAVERSE THROUGH LIST
    column_name = []
    column_datatype = []
    column_null = []
    prim_key_index = 10 #in case there is no prim key, error will be generated since default prim key value is assigned i.e later overwritten
    print("column:", columns[0])
    for x in range(len(columns)):
        column_name.append(columns[x][0])
        # decode is used to convert source_table_details i.e binary in string
        # In case of incorrect datatype error occurs etc, readjust this line according to usecase.
        column_datatype.append(re.split("'",str(re.split("'",columns[x][1].decode()))))
        column_datatype[x] = column_datatype[x][1]
        column_null.append(columns[x][2])
        if columns[x][2] == 'NO':
            column_null[x] = 'NOT NULL'
        elif columns[x][2] == 'YES':
            column_null[x] = 'NULL'
        if columns[x][3] == 'PRI':
            prim_key_index = x
            # this code does not currrently deal with unique keys.
            # code does not cater to cases where there is no primary key for now
    print("Primary key index: ", prim_key_index)
    table_existence_bool = check_table(cursor_destination, table_name)
    print("Value of table_existence_bool: ", table_existence_bool)
    if table_existence_bool == 0:
        query = create_query_construct(column_name, column_datatype, column_null, prim_key_index,table_name)
        cursor_destination.execute(query)
        fetch_and_insert(cursor_source,cursor_destination,column_name,table_name,conn2,source_database,destination_database,table_name_dest,connection_type,pipeline_type,column_datatype)
    elif table_existence_bool == 1:
        fetch_and_insert(cursor_source,cursor_destination,column_name,table_name,conn2,source_database,destination_database,table_name_dest,connection_type,pipeline_type,column_datatype)


if __name__=="__main__":
    connection()