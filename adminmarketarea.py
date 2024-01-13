#IMPORTING OUR ADMIN AND ACCOUNTS FILES FROM SHARED FILE
from shared import file_admin, file_name
from market import market_user_menu
#WE SET OUR OWN SEPERATOR TO WRITE  DATA IN FILE 
separated = "$$$#%"       

#setting our menu list as empty we already write 10 items in file that initially show to user
#and then when admin makes changes it reflects
menu_list=[]


# Reading from the file

with open(file_admin) as file:
    file.seek(0)
    for line in file:      # loop on lines of file
        products=line.split(f"{separated}")        # split to make list on our fix seperator

        #Appending dictionaries of menu in menu list 
        menu_list.append({products[0]:(int(products[1])),products[2]:(int(products[3]))})


#MAKING A FUNCTION FOR ADMIN TO ADD PRODUCT UT ALSO SAVE IN  FILE PERMENANTLY
def admin_add_product(menu_list):
    market_user_menu(menu_list)
    while True:
       try:      #using try accept to avoid crush

         # asking admin that ow many product he want to add
         how_much_prod=int(input("Enter How Many Products You Want To Add In Menu List (enter 0 to return to main menu) :"))
         if how_much_prod=="0":    # setting a condition if admin enter 0 then return back
            return
         break
       except ValueError:
          print("Inavlid Input Write In Digits")
    # applying loop to take input by admin as he told about how many products
    for num in range(1,how_much_prod+1):
        while True:                 # do in upper as in our dictionary it is all in uppercase
         name_prod=input(f"Enter Name Of {num} Product To Add:").upper()
         if name_prod.strip():
          # checking the condition that if admin enter any product that is already in menu  list
          #to avoid overwriting keys in our menu list
          for check in menu_list:
            if name_prod in check:
               print(f"This {name_prod} Is Already In Your List")               
               break
          else:
             break
         else:
            print("This Should Not Remain Empty")
        while True:
            try:        # taking inpuut of price of product
               price_prod=int(input(f"Enter Price Of {num} Product You Want To Set:"))
               if price_prod>0:       # checking that price of product must be graeter than zero

                break
               else:
                  print("Price Must Be Greater Than Zero")
            except ValueError:
               print("Price Must Be In Digits. And It Is Not Remain Blank")
        while True:
            try:

              # taking input of quantity by admin
               quantity_prod=int(input(f"Enter Quantity Of {num} Product You Want To Set:"))
               if quantity_prod>0:
                break
               else:
                  print("Quantity Must Be Greater Than Zero")
            except ValueError:
               print("Quantity Must Be In Digits. And It Is Not Remain Blank")
        # appending the product in menu list
        menu_list.append({name_prod:price_prod,"QUANTITY":quantity_prod})    
        #write the update in file permenantly as it reflects afterwards
        with open(file_admin, "w+") as file:
           for every in menu_list:           

            # use join so the every dictionary in a one line
            line = separated.join([f"{key}{separated}{value}" for key, value in every.items()])
            file.write(f"{line}\n")
        print("Item Is Added In Your Store List")
        print()
        print()
        market_user_menu(menu_list)   # calling it to update admin about product list

#making a function to tell admin about add stock options
def add_stock_intro():
    print("\tThere Are Two Choices For You,")
    print("\t1.Change Stock Of Entire List")
    print("\t2.Change Stock Of Specific Product")
    print("\t3.Exit From This Option")
    print()
    print()
def admin_add_stock(menu_list):
   while True:
      add_stock_intro()
      print()
      choice = input("Enter Your Choice:")        #taking choice as we define choice above
      if choice == "1":      # working on that if admin choice select 1
         market_user_menu(menu_list)
         print()
         while True:
            try:   # use try except to avoid crush

               # taking input of new quantity by admin
               new_quantity = int(input("Enter New Quantity To Set For All Products (enter 0 to back to menu): "))
               #checing if 0 enter return admin to main page
               if new_quantity == 0:
                  print("Back To Main Page")
                  print()
                  return
                # checking quantity must be greater than zero
               if new_quantity > 0:
                  break
               else:
                  print("Quantity Must Be Greater Than Zero")
            except ValueError:
               print("Quantity Must Be In Digits. It Is Not Remain Blank")
         # we simply set fix as our variable in which we fix our key
         fix = "QUANTITY"
         for check in menu_list:
            check[fix] = new_quantity     # update quantity as entered by admin

         print("Updated Stock List Is:")
         print()
         print()
         print()

         # write the update in file the changed made by admin
         with open(file_admin, "w+") as file:
           for every in menu_list:
            line = separated.join([f"{key}{separated}{value}" for key, value in every.items()])
            file.write(f"{line}\n")
         market_user_menu(menu_list)  # Use the updated menu_list here
         print()
         print()

    # now applying condition on choice 2
      elif choice == "2":
         market_user_menu(menu_list)
         print()
         print()
         fix = "QUANTITY"
         while True:
            # taking specific product name by admin
            product_name = input("Enter Product Name Whose Stock You Want To Increase (enter 0 to back to menu): ").strip().upper()
            if product_name == "0":
               print("Back To Main Page..")
               print()
               return
            #checking that product name must be in menu list to update quantity
            for check in menu_list:
               if product_name in check:
                  while True:
                     try:
                        #taking input of new quantity
                        new_quantity = int(input("Enter New Quantity You Want To Set: "))
                        if new_quantity > 0:
                           break
                        else:
                           print("Quantity Must Be Greater Than Zero")
                     except ValueError:
                        print("Quantity Must Be In Digits. It Is mandatory To Fill It.")
                  check[fix] = new_quantity          #update new QUANTITY
                  print("Updated Stock List Is:")
                  print()
                  #write permenantely in file
                  with open(file_admin, "w+") as file:
                    for every in menu_list:
                     line = separated.join([f"{key}{separated}{value}" for key, value in every.items()])
                     file.write(f"{line}\n")
                  market_user_menu(menu_list)  # Use the updated menu_list here
                  print()
                  print()
                  break
            else:
               # if product anme is not in menu list
               print(f"This Product {product_name} Is Not In Your STORE List ")
      elif choice == "3":              # exit to main page
         print("Back To Main Menu..")
         print()
         print()
         break
      else:
         print("Invalid Choice. Please Enter Correct Choice")
         print()
 
 #making a function for admin delete stock

#making a function for update price
def admin_price_setup(menu_list):
   while True:
      market_user_menu(menu_list)
      print()
      print()
      #taking input of product name to update price
      product_name = input("Enter Product Name You want To Change price Of (enter 0 to back to menu): ").strip().upper()
      if product_name == "0":
         return
      for check in menu_list:
         if product_name in check:
            while True:
               try:
                #taking input of new price admin wants to set
                  new_price = int(input("Enter New Price Of That Product (enter 0 to Go Back To Menu): "))
                  if new_price == 0:
                     return
                  if new_price > 0:
                     break
                  else:
                     print("Price Must Be Greater Than Zero.")
               except ValueError:
                  print("Price Must Be In Digit. It Is Mandatory To Fill It")

            for item in menu_list:
               if product_name in item:       # update new pprice in menu list
                  item[product_name] = new_price

            print("Updated List Of Store:")
            print()
            print()
            #write update in file
            with open(file_admin, "w+") as file:
             for every in menu_list:
              line = separated.join([f"{key}{separated}{value}" for key, value in every.items()])
              file.write(f"{line}\n")
            market_user_menu(menu_list)  # Use the updated menu_list here
            print()
            print()
            break

      else:
         print(f"This Product {product_name} Is Not In Your Store List")        

def admin_delete_product(menu_list):
    while True:
        market_user_menu(menu_list)
        print()
        print()
        #taking input of product name that admin wants to delete
        prod_name = input("Enter Product Name You Want To Delete From Menu List (Enter 0 To Go Back):").upper()
        if prod_name == "0":
            return
        # applying loop to check that product is in list or not?
        for check in menu_list:
            if prod_name in check:          # if product is found
                menu_list.remove(check)        # remove the product from list

                # writting the update permenantely in file
                with open(file_admin, "w+") as file:
                 for every in menu_list:
                  line = separated.join([f"{key}{separated}{value}" for key, value in every.items()])
                  file.write(f"{line}\n")
                market_user_menu(menu_list)
                print()
                print()
                print(f"Item {prod_name} Deleted Successfully From Your Store.")
                print()
                print()
                break
        else:
            # This block will only execute if the loop completes without a break, meaning the product was not found
            print(f"This Item {prod_name} Is Not In Your Menu Of Store")
            print()
            print()









