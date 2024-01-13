from shared import file_name, file_admin
from market import user_info, user_delete, market_user_menu, add_cart, user_list, price_list, user_bill, view_cart, see_history


final=[]
def login(final, file_market,menu_list):
    x = "@#$!"
    try:
      with open(file_name) as file:
        user_data = []
        for line in file:
            data = line.strip().split(f"{x}")
            user_dic = {"username": data[0], "password": data[1], "passwordhint": data[2]}
            user_data.append(user_dic)
    except FileNotFoundError:
       print("File Not Found")
    while True:
        user_name = input("Enter Your User Name: ")
        user_name_check = False

        for every in user_data:
            if user_name == every["username"]:
                user_name_check = True
                file_market = file_market + user_name + ".txt"
                while True:
                 password = input("Enter Your Password: ")
                 if password == every["password"]:
                    print("Login Successfully")
                    while True:
                        user_info()
                        print()
                        option = input("Enter Your Options: ")
                        print()
                        if option == "1":
                            market_user_menu(menu_list)
                        elif option == "2":
                            add_cart(menu_list, user_list)
                        elif option == "3":
                            user_delete(menu_list, user_list, price_list)
                        elif option == "4":
                            view_cart(user_list, menu_list)
                        elif option == "5":
                            user_bill(menu_list, user_list, file_market,file_admin)               
                        elif option == "6":
                            see_history(menu_list,user_list,file_market) 
                        elif option == "7":
                            print("Program Is Exiting .")
                            print("Thank You For Visting COMPUTER ZONE!!")                          
                            return        
                        else:
                            print("Invalid Choice. Please select a correct choice.")
                            continue
                 else:
                    print("Invalid Password")
                    print(f"Password Hint: {every['passwordhint']}")
                    while True:
                     user_ask = input("Do you want to continue? (yes/no): ").lower()
                     if user_ask == "no":
                        print("Back To Main Page")
                        return
                     elif user_ask=="yes":
                        print("Alright Try Again!!")
                        break
                     else:
                        print("please Enter Correct Word Yes Or No")
                  
        if not user_name_check:             
             print("Invalid Username. Please try again.")
             while True:
              ask_for_try=input("Did You Want Another Try? (yes/no) ").lower()
              if ask_for_try=="no":
                 print()
                 print("Back To Main Page")
                 print()
                 return
              elif ask_for_try=="yes":
                 print()
                 print("Alright Try Again!")
                 print()
                 break
              else:
                 print("Please Enter Correct Word Yes Or No")
                 print()