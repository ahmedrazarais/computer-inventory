# main.py
#IMPORTING ALL FILES IN MAIN FILE
from shared import file_market
from signup import signup
from adminmarketarea import menu_list
from login import login
from adminlogin import admin_login

final = []
def choice_user():                      # Make a function for our homepage
                                         # provide information to users   
   print("\tMain Page Of Computer Gala")
   print()
   print("Once You Login You Are Able To Enter In COMPUTER ZONE STORE.")

   print("\t1.Signup As User")
   print("\t2.Login As User")
   print("\t3.Login As Admin")
   print("\t4.To Exit")   
   print()
print("\tWelcome To Computer Gala")

while True:
   choice_user()                       # Applying conditions as we provide information to user above
   choice=input("Enter Your Choice:")
   if choice=="1":
      print()
      print("Create Your Account")
      print()

      signup(final)
   elif choice=="2": 
      print("Now You Can Login..")
      print()
      login(final,file_market,menu_list)
   elif choice=="3":
      admin_login(final)
   elif choice=="4":
      print("Catch you later! The application is heading out")
      break
   else:
      print("Invalid Choice")
      print()
   