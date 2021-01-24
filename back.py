import psycopg2
from psycopg2 import sql
import json




conn = psycopg2.connect(dbname='flask',user='postgres',password='123456789',host='localhost')
cursor = conn.cursor()
def create_db():
	cursor.execute(""" CREATE TABLE Nur 
       (ID TEXT NOT NULL,
         AUTHOR TEXT NOT NULL,
         DATA INT NOT NULL,
         CONTENT TEXT NOT NULL
         );"""
         )
	print('TABLE CREATED')
	conn.commit()
	conn.close()
def POST(id,author,date,content):
	query = "INSERT INTO Nur (ID,AUTHOR,DATA,CONTENT) VALUES (%s,%s,%s,%s)"
	cursor.execute(query,(id,author,date,content))
	conn.commit()
	print('INSERTED')
	conn.close()
	return ':D'
def GET():
    cursor.execute('SELECT content FROM Nur')
    rows = cursor.fetchall()
    print(rows)    
def GET_BY_ID(id):
	query = 'SELECT content FROM Nur WHERE id=%s'
	cursor.execute(query,(id,))
	print(cursor.fetchone())
	return ':)'


def PUT(id_to_change,id,author_to_change,author,date_to_change,data,content_id,content):
	query = "UPDATE Nur SET ID = %s WHERE ID = %s"
	cursor.execute(query,(id,id_to_change))
	conn.commit()
	print('UPDATED ID')

	query = "UPDATE Nur SET AUTHOR = %s WHERE AUTHOR=%s"
	cursor.execute(query,(author_to_change,author))
	conn.commit()
	print('updated author')

	query = "UPDATE Nur SET DATA=%s WHERE DATA=%s"
	cursor.execute(query,(date_to_change,data))
	conn.commit()
	print('updated data')

	query = "UPDATE Nur SET CONTENT=%s WHERE ID=%s"
	cursor.execute(query,(content,content_id))
	conn.commit()
	print('updated data')

	conn.close()
	return ':D'

def DELETE(id):
	query = "DELETE FROM Nur WHERE ID = %s"
	cursor.execute(query,(id,))
	conn.commit()
	print('UPDATED ID')
	conn.close()
	return ':D'





