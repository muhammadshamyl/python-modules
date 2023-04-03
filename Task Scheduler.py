import mysql.connector as mysql
import time,os, multiprocessing, psutil
from datetime import datetime


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

def pipeline_profile_connection():
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


def process_check(result):
    print("Process ID: ", os.getpid() ," -------  ID: " , result[0])

def proc_exec(result):
    now = datetime.now()
    result = list(result)
    if result[1] != None and result[2] == None:
        time.sleep(1)
        print("Process ID: ", os.getpid() ," Condition being met" , result)
        print("Process ID: ", os.getpid() ," -------  ID: " , result[0])
        # setting bool to 1 which means activation of dedicated pipeline
        result[3] = 1
        dpl_bool(result)
        # enter script for calling dedicated dpl script
        # if result[3] == 1:
        #     dpl_bool(result)
    elif result[2] != None and result[1] == None:
            if now.strftime("%H") == result[2].strftime("%H") and now.strftime("%M") == result[2].strftime("%M"):
                result[3] = 1
                print("Condition met.")
                dpl_bool(result)
            # else:
            #     print("Condition not met.")
    
def dpl_bool(result):
    print("Trigger bool at DPL id:" ,result[0]," pid ", os.getpid(), " is ",result[3])
    # loading delta from source
    print("Process ID: ", os.getpid(), "going to sleep")
    connection_type = trigger_pipeline(result[0])
    print("DPL Script to trigger: ", connection_type)
    if isinstance(connection_type,str): 
        print(connection_type)

    pipeline_activation(connection_type)
    
        
    if result[1] != None:# and result[2] == None:
        time.sleep(result[1])
    
    print("Resetting bool to 0. Process ID: ",os.getpid())
    result[3] = 0
    print("Trigger bool at id:( " ,result[0]," pid ", os.getpid(), " is now ",result[3])


def pipeline_activation(connection_type):
    if connection_type == "mysql-mysql":
        import mysql2mysql as my2my
        my2my.my2my_greet()
    elif connection_type == "psql-mysql":
        import psql2mysql as p2my
        p2my.p2my_greet()
    
    elif connection_type == "mysql-psql":
        import mysql2psql as my2p
        my2p.my2py_greet()
    elif connection_type == "mongo-psql":
        import mongo2psql as mon2p
        mon2p.mon2p_greet
    elif connection_type == "mongo-mysql":
        import mongo2mysql as mon2my
        mon2my.mon2my_greet


def trigger_pipeline(pipeline_id):
    # print("Condition entered")
    pipeline_conn = pipeline_profile_connection()
    pipeline_cursor = pipeline_conn.cursor()
    pipeline_cursor.execute("select database();")
    pipeline_cursor.fetchone()
    query = ("select * from pipeline_profile where id = {id};").format(id=int(pipeline_id))
    print("query: ", query)
    try:
        pipeline_cursor.execute(query)
        pipelines = pipeline_cursor.fetchone()
        if pipelines != None and len(pipelines) > 0:
            print(pipelines)
            return pipelines[3]
        else:
            print("Pipeline not found against pipeline id:",pipeline_id)
            return 0
    
    except (mysql.Error, mysql.Warning) as e:
        print("Mysql error: ", e)
        return e

    # print("Pipeline to trigger: ", pipelines[0])

    # if pipeline_id == 1:
        # print("query: ", query)
        # pipeline_cursor.execute(query)
        # pipelines = pipeline_cursor.fetchall()

        # print("Pipeline to trigger: ", pipelines[0])
    return
def TS_DB():
    print("Updating task scheduler object")
    conn_scheduler = task_scheduler_connection()
    cursor_scheduler = conn_scheduler.cursor()
    cursor_scheduler.execute("select database();")
    cursor_scheduler.fetchone()
    cursor_scheduler.execute("select * from scheduler")
    result = cursor_scheduler.fetchall()
    return result

def scheduler_main():
    i = 0
    pool = multiprocessing.Pool()
    result = TS_DB()
    while i < 6:
        pool.map(proc_exec,result)
    pool.close


    
if __name__=="__main__":
    scheduler_main()