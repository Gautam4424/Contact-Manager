import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",passwd="Gautam@4424",database="contacts")
cur=connection.cursor()
def update():
    Name=input("Enter the Name you Want to upadate : ")
    try:
        cur.execute("Select * from contacts where name='{}'".format(Name))
        contacts=cur.fetchall()
        if contacts!=[]:
            print(contacts)
            num=input("Enter the number which you want to change :")
            num2="+91"+num
            cur.execute("Select * from contacts where phone_number='{}'".format(num2))
            numb =cur.fetchall()
            print("1.Name",end=" ")
            print("2.Phone Number",end=" ")
            print("3.All")
            choise=int(input("Enter Your Choise :"))
            if choise==1:
                new_name=input("Enter the new name of this contact :")
                confirm=int(input("press 1 to continue :"))
                if confirm==1:
                    try:
                        cur.execute("update contacts set name='{}' where Phone_number='{}' ".format(new_name,num2))
                        connection.commit()
                        print("Name Change Successfully")
                    except Exception as e:
                        print("Error to change the Name!!")
                else:
                    print("There is something Wrong Try again!!")
            elif choise==2:
                new_num= input("Enter the new number of this contact :")
                num3="+91"+new_num
                confirmation = int(input("press 1 to continue :"))
                if confirmation==1:
                    try:
                        cur.execute("update contacts set Phone_number='{}' where Phone_number='{}' ".format(num3,num2 ))
                        connection.commit()
                        print("Number Change Successfully")
                    except Exception as e:
                        print("Error to change the Number!!")
                else:
                    print("There is something Wrong Try again!!")
            elif choise==3:
                new_Name = input("Enter the new name of this contact :")
                new_number = input("Enter the new number of this contact :")
                num4 = "+91" + new_number
                confirmation = int(input("press 1 to continue :"))
                if confirmation == 1:
                    try:
                        cur.execute("update contacts set Phone_number='{}',name='{}' where Phone_number='{}' ".format(num4,new_Name, num2))
                        connection.commit()
                        print(" Name,Number Change Successfully")
                    except Exception as e:
                        print("Error to change the Number,Name!!")
                else:
                    print("There is something Wrong Try again!!")
        else:
            print("Contact Not found!!")
    except Exception as e:
        print(e)

