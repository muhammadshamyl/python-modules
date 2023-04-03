import mysql.connector as mysql
import time,os, multiprocessing, psutil
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

def process_check(result):
    print("Process ID: ", os.getpid() ," -------  ID: " , result[0])

def proc_exec(result):
    result = list(result)
    if (result[1] != None):
        time.sleep(1)
        print("Process ID: ", os.getpid() ," Condition being met" , result)
        # proc_exec(result)
        print("Process ID: ", os.getpid() ," -------  ID: " , result[0])
        result[3] = 1
        # enter script for calling dedicated dpl script
        if result[3] == 1:
            dpl_bool(result)
        # result = 
    
def dpl_bool(result):
    print("Trigger bool at DPL id:" ,result[0]," pid ", os.getpid(), " is ",result[3])
    print("Process ID: ", os.getpid(), "going to sleep")
    time.sleep(result[1])
    print("Resetting bool to 0. Process ID: ",os.getpid())
    result[3] = 0
    print("Trigger bool at id: " ,result[0]," pid ", os.getpid(), " is now ",result[3])
    # return

def TS_DB():
    print("Updating task scheduler object")
    conn_scheduler = task_scheduler_connection()
    cursor_scheduler = conn_scheduler.cursor()
    cursor_scheduler.execute("select database();")
    # scheduler_database = cursor_scheduler.fetchone()
    cursor_scheduler.fetchone()
    cursor_scheduler.execute("select * from scheduler")
    result = cursor_scheduler.fetchall()
    return result

def scheduler_main():
    i = 0
    pool = multiprocessing.Pool()
    # pool2 = multiprocessing.Pool()
    result = TS_DB()
    while i < 6:
        pool.map(proc_exec,result)
        # pool2.map(TS_DB,)
    pool.close


    
if __name__=="__main__":
    scheduler_main()