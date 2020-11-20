import mysql.connector
from phonenumbers import carrier
import phonenumbers
connection=mysql.connector.connect(host="localhost",user="root",passwd="Gautam@4424",database="contacts")
cur=connection.cursor()
def add_number():
    loop=int(input("How many phone number you want to add : "))
    for i in range(loop):
        Phone=input("Enter phone number : ")
        p=("+91"+Phone)
        phone_num=phonenumbers.parse(p)
        car=carrier.name_for_number(phone_num,lang="eng")
        Name=input("Enter name : ")
        print(Phone)
        print(car)
        print(Name)
        confirmation=int(input("press 1 to continue :"))
        if confirmation==1:
            try:
                cur.execute("INSERT INTO contacts (Name,phone_number,carrier) values('{}','{}','{}')".format(Name,p,car))
                connection.commit()
                print("Added successfuly")
            except Exception as e:
                print(e)
                print("Something Went wrong !!")
        else:
            print("select Valid Option")

