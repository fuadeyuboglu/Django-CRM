import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Zxv^*&^Bv1b83-8x'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE supplies")

print("All Done!")