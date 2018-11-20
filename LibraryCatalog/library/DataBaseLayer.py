
import pymysql
from contextlib import closing



def connectDb():
    conn = pymysql.Connect(host='localhost', port=3306, user='root', password='Admin123', db='soen341')
    return conn



def insertCommand(insertcmd):
    # Connect to the database
    conn = connectDb()
    try:
        with conn.cursor() as curr:
            curr = conn.cursor()
            # Execute the Insert Command against the MY SQL Server
            curr.execute(insertcmd)
            conn.commit()
    finally:
        # Close the connection of the database
        conn.close()
    return conn.insert_id()


def updateCommand(updatecmd):
    # Connect to the database
    conn = connectDb()
    try:
        with conn.cursor() as curr:
            curr = conn.cursor()
            # Execute the Update Command against the MY SQL Server
            curr.execute(updatecmd)
            conn.commit()
    finally:
        # Close the connection of the database
        conn.close()
    return conn.insert_id()


def selectCommand(selectCmd):
    # Connect to the database
    conn = connectDb()
    try:
        with conn.cursor() as curr:
            curr.execute(selectCmd)
            tables = curr.fetchall()
            conn.commit()
            return tables
    finally:
        conn.close()


def deleteCommand(deletecmd):
    # Connect to the database
    conn = connectDb()
    try:
        with conn.cursor() as curr:
            curr = conn.cursor()
            # Execute the Delete  Command against the MY SQL Server
            curr.execute(deletecmd)
            conn.commit()
    finally:
        # Close the connection of the database
        conn.close()
    return conn.affected_rows()


# def printTable(tables):
#     for row in tables:
#         for item in row:
#             print(item)

#
# def last_id_inserted():
#
#     return conn.insert_id()



