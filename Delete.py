import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="Gautam@4424",database="contacts")
cur=connection.cursor()
def delete():
     Name=input("Enter the name :")
     cur.execute("select * from contacts where Name='{}'".format(Name))
     output = cur.fetchall()
     print(output)
     if output!=[]:
         num=input("Enter the number you want to delete :")
         n1="+91"+num
         cur.execute("select * from contacts where Phone_number='{}'".format(n1))
         v=cur.fetchall()
         if v!=[]:
             cur.execute("Delete from contacts where phone_number='{}'".format(n1))
             connection.commit()
             print("Delete successfuly")
         else:
             print("please enter valid number!!!")
     else:
         print("Entry Not found")