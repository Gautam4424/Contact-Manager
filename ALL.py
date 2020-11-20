import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="Gautam@4424",database="contacts")
cur=connection.cursor()
def show_all():
    cur.execute("select * from contacts")
    output=cur.fetchall()
    print(output)