import mysql.connector

def conectarBanco():
    mydb = mysql.connector.connect(
        host="localhost",
        user="cuidador",
        password="Cuidador@25",
        database="cuidadores"
    )
    return mydb


