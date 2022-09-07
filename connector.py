import mysql.connector


def SQL_Connector():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="xxxxxxx",
    database="clientes"
  )

  return mydb


