
import pymysql
from contextlib import closing


def connectDb():
    conn = pymysql.Connect(host='localhost', port=3306, user='root', password='Admin123', db='soen341')
    return conn


def insertCommand(conn, insertcmd):
    curr=conn.cursor()
    curr.execute(insertcmd)
    conn.commit()


def selectCommand(conn, selectCmd):
    curr = conn.cursor()
    curr.execute(selectCmd)
    tables = curr.fetchall()
    conn.commit()
    return tables

def printTable(tables):
    for row in tables:
        for item in row:
            print(item)


