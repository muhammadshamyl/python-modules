import importScript as p2
import mysql.connector as mysql
import datetime, re
from datetime import datetime
import time

# def playdo():
#     print("hello playdo")
#     alpha = p2.text() + 10
#     print(alpha)

#     return


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

def scheduler():
    now = datetime.now()
    hour = now.strftime("%H")
    
    print("System time: ", now)
    print("Hour:", hour)
    
    conn_scheduler = task_scheduler_connection()
    cursor_scheduler = conn_scheduler.cursor()
    cursor_scheduler.execute("select database();")
    cursor_scheduler.fetchone()
    cursor_scheduler.execute("select * from scheduler")
    result = cursor_scheduler.fetchall()
    now = datetime.now()
    print("Current Time: ", now)
    sec = now.strftime("%H")
    print("Seconds: ", sec)
    for x in result:
    
        if x[2] != None:
            if now.strftime("%H") == x[2].strftime("%H") and now.strftime("%M") == x[2].strftime("%M"):
                print("Condition met.")
            else:
                print("Condition not met.")
            
if __name__=="__main__":    
    # playdo()
    i = 0
    while i < 2:
        scheduler()
        

