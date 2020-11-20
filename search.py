import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="Gautam@4424",database="contacts")
cur=connection.cursor()
def search():
    Name=input("Enter the name you want to search : ")
    cur.execute("select * from contacts where Name='{}'".format(Name))
    output=cur.fetchall()
    print(output)