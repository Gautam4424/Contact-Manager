import Add
import search
import Delete
import update
import ALL
print("Welcome to contact manager \n created by Gautam Sachdeva")
print("1.Add contact",end="  ")
print("2.Search contact",end="  ")
print("3.Delete contact",end="  ")
print("4.Update contact",end="  ")
print("5.Show all")
option=int(input("Enter your choise : "))
if option==1:
   Add.add_number()
elif option==2:
    search.search()
elif option==3:
    Delete.delete()
elif option==4:
    update.update()
elif option==5:
    ALL.show_all()
else:
    print("Please choose valid option!!")
