import mysql.connector as mysql


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

def testScript(pipeline_id):
    cursor = pipeline_profile_connection()
    cursor_pipeline = cursor.cursor()
    cursor_pipeline.execute("select database();")
    cursor_pipeline.fetchone()
    query = ("select * from pipeline_profile where id = {id};").format(id = pipeline_id)
    cursor_pipeline.execute(query)
    result = cursor_pipeline.fetchall()
    print(result) 
if __name__ == "__main__":
    id = 1
    testScript(id)
    