from time import time
import schedule
from datetime import date, datetime
import mysql.connector as mysql

def callme():
    # now = datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    print("I am invoked!")
    conn_scheduler = task_scheduler_connection()
    cursor_scheduler = conn_scheduler.cursor()
    cursor_scheduler.execute("select database();")
    scheduler_database = cursor_scheduler.fetchone()
    print(scheduler_database[0])

    conn_pip = pipeline_connection()
    cursor_pipeline = conn_pip.cursor()
    cursor_pipeline.execute("select database();")
    pipeline_database = cursor_pipeline.fetchone()
    # print(pipeline_database)
    cursor_pipeline.execute("show tables;")
    pipeline_profile = cursor_pipeline.fetchall()
    # print(pipeline_profile)
    pipeline_profile = pipeline_profile[1][0]
    print(pipeline_profile)
    # x = datetime.now()
    # print(x.hour,":",x.minute,":",x.second)
    # print(pipeline_profile)
    # # cursor_pipeline.execute("show columns from " + pipeline_profile + ";")
    # cursor_pipeline.execute("select * from " + pipeline_profile + ";")
    # table_det = cursor_pipeline.fetchall()
    # pipeline_id_list = []
    # for x in table_det:
    #     print(x)
    #     pipeline_id_list.append([x[0],x[1],x[2],x[3],x[6],x[7],x[8],x[9]])
    
    # print("pipeline id's : ", pipeline_id_list)



    
interval_time = 2
interval_period = "seconds"

def scheduler(interval_time,interval_period):
    if interval_period == "seconds":
        schedule.every(interval_time).seconds.do(callme)
    elif interval_period == "minutes":
        schedule.every(interval_time).minutes.do(callme)
    elif interval_period == "hours":
        schedule.every(interval_time).hours.do(callme)
    elif interval_period == "days":
        schedule.every(interval_time).days.do(callme)
    elif interval_period == "weeks":
        schedule.every(interval_time).weeks.do(callme)    
    
    while True:
        schedule.run_pending()
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

def scheduler_main():
    scheduler(interval_time,interval_period)
    
if __name__=="__main__":
    scheduler_main()