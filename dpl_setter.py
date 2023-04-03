import mysql.connector as mysql
def task_scheduler_connection():
    try:
        conn = mysql.connect(
        host= 'localhost',
        user='root',
        password='root123',
        db='task_scheduler'
        )
        print("task_scheduler database connected.")
        return conn

    except:
        print("Pipeline connection failed to be established")

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

def dplTrigger(var):
    profile_check_bool = None
    table = None
    print("Enter eye of the dragon")
    pip_conn = pipeline_connection()
    ts_conn = task_scheduler_connection()
    ts_cursor = ts_conn.cursor() 
    pipeline_cursor = pip_conn.cursor()
    # just checking connection
    # pipeline_cursor.execute("show tables;")
    # tables = pipeline_cursor.fetchall()
    # print("Tables: ")
    # for x in tables:
    #     print (x[0])
    pipeline_cursor.execute("show tables;")
    tables = pipeline_cursor.fetchall()
    for x in tables:
        print(x[0])
        if x[0] == "pipeline_profile":
            print("--------------------------------------")
            table = str(x[0])
    
    pipeline_cursor.execute("select * from " +table+ ";")
    records = pipeline_cursor.fetchall()
    for x in records:
        print(x)
        if x  == var:
            print("IF condition met.")
            profile_check_bool = 0
        
        elif x != var:
            print("elif condition met.")
            profile_check_bool = 1
    
    if profile_check_bool == 1: #bool is supposed to be at 1. This is just to check
        # pipeline_cursor.execute("insert into pipeline_profile;")
        print("bool condition entered.")
        query = insert_query_construct(var,table)
        pipeline_cursor.execute(query,var)
        # pip_conn.commit()
    
    elif profile_check_bool == 0:
        print("bool condition not entered.")
        print("Profile attempted to be entered into pipeline_profile already pre-exists.")

    return

def insert_query_construct(var,table):
    loop_counter = 0
    query = "INSERT INTO " + table + "(id,source_table,destination_table,connection_type,pipeline_type,cycles,source_database,destination_database,assigned_time,fixed_frequency) VALUES("
    for x in var:
        print("----------------------------------------------------")
        print(x)
        query = query + "%s"
        loop_counter = loop_counter + 1
        if loop_counter  <  len(var):
            query = query + ","
     
    query = query + ")"   
    print("query:", query)
    return query

if __name__=="__main__":
    var = (2, 'customers', 'customers', 'mysql-mysql', 'ETL', 85, 'classicmodels', 'classic_replica', None, 30)
    dplTrigger(var)