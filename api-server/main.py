from fastapi import FastAPI
import mysql.connector
from mysql.connector import Error

app = FastAPI()

@app.get("/")
def choose_query():
    return {"message": "Hello, enter query in url"}

@app.get("/by-firstname/")
def get_people_firstname(first_name:str=""):
    query = "select * from people"
    if first_name != "":
        query+=" where first_name='"+first_name+"'"
    query+=";"

    res = execute_query(query)
    return {"results": res}

@app.get("/by-lastname/")
def get_people_lastname(last_name:str=""):
    query = "select * from people"
    if last_name != "":
        query+=" where last_name='"+last_name+"'"
    query+=";"

    res = execute_query(query)
    return {"results": res}

@app.get("/everyone/")
def get_people():
    query = "select * from people;"
    res = execute_query(query)
    return {"results": res}

def execute_query(query):
    try:
        conn = mysql.connector.connect(host='rds_instance_endpoint_here', database='bazepodataka', user='appuser', password='appuser')

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            return results

    except Error as e:
        print("error", e)

    except Exception as e:
        print("Error executing query ", e)

    finally:
        if (conn and conn.is_connected()):
            conn.commit()
            cursor.close()
            conn.close()