from signup import signup
from adminmarketarea import admin_add_product, admin_add_stock, admin_delete_product, admin_price_setup, menu_list
from adminuserarea import search_any_account, see_all_data, delete_account


def info_admin():
    print("\t1.Manage Accounts Of Users")
    print("\t2.Manage Shopping Mart For Users")
    print("\t3.To Exit")
    print()      
def account_admin():
    print("\t1. Add Any Account")
    print("\t2. Search any  Account")
    print("\t3. See All Data")
    print("\t4. Delete any Account")
    print("\t5. Exit Out From This Section") 
    print()

def market_admin():
    print("\t1. Add Any Product In Your Store")
    print("\t2. Update Stock Of Your Products ")
    print("\t3. Update Prices Of Your Products")
    print("\t4. Delete Any Product From Your Store ")
    print("\t5. Exit  from This Section")
    print()

def admin_login(final):
   x="@#$!"
   admin_user_name="drmaria"
   admin_psd="1234"
   user_username_input=input("Enter Admin User Name:")
   User_Password_input=input("Enter  Admin Password:")
   print()
   if user_username_input==admin_user_name and User_Password_input==admin_psd:
      print("\t\tWELCOME TO ADMIN PAGE")
      while True:
         info_admin()
         print()
         choice=input("Enter Your Desired Option:")
         if choice=="1":           
             while True:
                account_admin()
                option=input("Enter Your Option What You Want To Do :")
                if option=="1":
                    signup(final)
                elif option=="2":
                    search_any_account(final)
                       
                elif option=="3":
                    see_all_data(final)

                elif option=="4":
                    delete_account(final)

                elif option=="5":
                    print("You Are Out From This Section")
                    break
                else:
                    print("Invalid Choice")
                    print()
         elif choice=="2":
              while True:
                 market_admin()
                 option=input("Enter Your Option What You Want To Do :")
                 if option=="1":
                    admin_add_product(menu_list)
                 elif option=="2":
                    admin_add_stock(menu_list)
                 elif option=="3":
                    admin_price_setup(menu_list)
                 elif option=="4":
                    admin_delete_product(menu_list)
                 elif option=="5":
                    print("You Are Out From This Section")
                    break
                 else:
                    print("Invalid Choice")
                    print()
         elif choice=="3":
              print("You Are Out From Admin Page")
              break
         else:
              print("Invalid Choice")
              print()
   else:
      print("Invalid Username or Password")
      print()



