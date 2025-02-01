import mysql.connector
"""
MySQL Access
root:Vicente@20025
cuidador:Cuidador@25
"""
def conectarBanco():
    mydb = mysql.connector.connect(
        host="localhost",
        user="cuidador",
        password="Cuidador@25",
        database="cuidadores"
    )
    return mydb


