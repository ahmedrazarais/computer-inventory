
separated = "$$$#%" 
#setting our menu list as empty we already write 10 items in file that initially show to user
#and then when admin makes changes it reflects
menu_list=[]

#This is our two list one is for user cart
#another is for appending the prices as we calculate bill for user
user_list=[]
price_list=[]


#market functions for user that tell information
def user_info():
   print("\t1.See Our Product List")
   print("\t2.Add  Item To Your Cart ")
   print("\t3.Delete Item From Your Cart")
   print("\t4.See Your Cart")
   print("\t5.Checkout From Application")
   print("\t6.See Your History")
   print("\t7. Exit Application")

# making a function to print menu list in standard form    
def market_user_menu(menu_list): 
    print(f"Welcome To Computer Zone".center(50))    # formatting to print in standard form
    print("{:<15} {:<15} {:<10}".format("Product", "Price (PKR)", "Quantity"))
    print("-" * 40)

    print()
    for items in menu_list:
        product = list(items.keys())[0]
        price = items[product]
        quantity = items["QUANTITY"]
        
        print("{:<15} {:<15} {:<10}".format(product, price, quantity))
    print()

#making an add cart function for user
def add_cart(menu_list, user_list):
    market_user_menu(menu_list)

    while True:
        # strip to remove whitespaces to reove misunderstanding
        # upper to match with our keys
        product_choice = input("Enter Product Name To Add In cart:").strip().upper()
        valid_product = False  # Flag to indicate if the product is valid

        # Check if the product is in the menu_list
        for details in menu_list:
            if product_choice in details:
                fix = "QUANTITY"
                # Check if the product is in stock
                if details[fix] > 0: # checking greater than zero condition
                    try:
                        #taking input of quantity
                        user_quantity_Ask = int(input(f"Enter Quantity How Many You want To Add In Cart? (Available: {details[fix]}): "))
                    except ValueError:
                        print("Invalid Quantity. Must Be In Digits")
                        valid_product = True      # check is now true
                        break

                    # Check if the user entered quantity is valid
                    if 0 < user_quantity_Ask <= details[fix]:
                        # Check if the product is already in the user's cart
                        for user_item in user_list:

                            #managing our menu list according to user choices
                            if user_item["Product"] == product_choice:
                                user_item["Quantity"] += user_quantity_Ask
                                user_item["Price"] += user_quantity_Ask * details[product_choice]
                                details[fix] -= user_quantity_Ask
                                print(f"Item {product_choice} Is Added To  Your Cart")
                                print()
                                print()
                                valid_product = True
                                break
                        else:
                            # If the product is not in the user's cart
                            user_list.append({"Product": product_choice, "Price": user_quantity_Ask * details[product_choice], "Quantity": user_quantity_Ask})
                            details[fix] -= user_quantity_Ask
                            print(f"Item {product_choice} Is Added To Cart")
                            valid_product = True
                        break  # Break out of the loop after processing the current product
                    else:
                        print("Invalid Quantity. Must be greater than 0 and less than or equal to available quantity.")
                        valid_product = True
                    break  # Break out of the loop after processing the current product
                else:
                    print(f"Not Enough Stock. {product_choice} is Out Of Stock.")
                    valid_product = True
                    break  # Break out of the loop after processing the current product

        # Print the message only if the product is not in the menu_list
        if not valid_product:
            print(f"This Product {product_choice} is Not in our Store")

        # Ask if the user wants to add more items
        while True:
            print()
            asking_for_more = input("Did You Want To Add More Items (yes/no) :").lower()
            print()
            if asking_for_more == "no":
                return  # Exit the function if the user does not want to add more items
            elif asking_for_more == "yes":
                break
            else:
                print("Please Select Correct Word [yes or no]")


def display_items(user_list):
    print("{:<15} {:<15} {:<10}".format("Product", "Price", "Quantity"))
    print("-" * 40)
    for items in user_list:
        product = items["Product"]       # display in standard form to user
        price = items["Price"]
        quantity = items["Quantity"]
        print("{:<15} {:<15} {:<10}".format(product, price, quantity))


def user_delete(menu_list, user_list, price_list):
    #checking if usercart is empty
    if not user_list:
       print("Your Cart Is Empty!!\n""There are no items in your cart.")
    else:
    # display user his cart
     print("Your Cart".center(38))
     display_items(user_list)
     print()
     
     delete_confirm=False       # intital it false
     while True:
      product_check = input("Enter Product Name You Want To Delete (0 To Return To Menu) :").upper()
      if product_check=="0":
         return
    # Keys of user cart list
      fix_prod = "Product"
      fix_quan = "Quantity"
      fix_price = "Price"
      product_found=False
      for check in user_list:
        if product_check in check[fix_prod]:
            product_found=True
            # ASKING QUANTITY IF PRODUCT FOUND
            while True:
             try:
               product_quan_check = int(input("Enter How Many Quantity You Want To Delete:"))
               break
             except ValueError:
              print("Quantity Must Be In digits")
            if check[fix_quan] >= product_quan_check:

                # Decrement user cart according to user input
                check[fix_quan] -= product_quan_check
                print(f"Item {product_check} Deleted From Cart with quantity {product_quan_check}")
                print()

                # Condition for taking the official price of the product and increment or decrement in quantities
                # Working to update the main menu list
                for every in menu_list:
                    if product_check in every:
                        # Getting the official price of the product
                        price = every[product_check]
                        price = product_quan_check * price

                        # Decrement price according to quantity from user cart
                        check[fix_price] -= price

                        # Update stock in our main menu
                        every["QUANTITY"] += product_quan_check
                if check[fix_quan] == 0:
                    user_list.remove(check)
                delete_confirm=True
                    # CLEARING THE LIST
                price_list.clear()
                    # EXTEND IT TO ITERATE OVER PRICES IN CART
                price_list.extend(cart_item[fix_price] for cart_item in user_list)
                break
            else:
               print("Quantity You Entered Is Bigger Than Quantity In your cart")
      if not product_found:
          print(f"{product_check} Is Not In your cart")
      if delete_confirm:
          break

# function for user cart display
def view_cart(user_list,menu_list):
   if not user_list:
      print("Looks like you haven't added anything to your cart yet.")
      print()
   else:   
    #if items in user cart
    print("Your Cart".center(38))
    display_items(user_list)


# user bill and checkout function
def user_bill(menu_list, user_list,file_market,file_admin):
    if not user_list:     # if emptty user cart
        print()
        print("Oops! It seems like you forgot to add items to your shopping cart.")
        print("Your Shopping Cart Is Empty!!")
        print()
        print()
        print()
        while True:  # ask by user for confirmation of checkout
           ask_by_user=input("Are You Sure You Want To Checkout (yes/no):").lower()
           if ask_by_user=="no":
              print()
              print("Alright Do Some Shopping!!")
              return
           elif ask_by_user=="yes":    # checking user choices
              print()
              print("Thank You For Visiting Computer Zone!!")
              exit()
           else:
              print("Please Select Correct Word")

    else: # if something in cart
        while True:
         ask_by_user=input("Are You Sure You Want To Do Check Out (yes/no) :").lower()
         if ask_by_user=="yes":
          print("Your Shopping Cart Is:")
          print()
          #open user file to write his cart in file that he is able to see his history
          with open (file_market,"a+") as file:
             view_cart(user_list, menu_list)

             #calculating bill
             bill = sum(cart_item["Price"] for cart_item in user_list)
             #import time to write in file of user
             import time
             current_time=time.ctime()

             #writting details in file
             file.write("\t\tHISTORY OF YOUR SHOPPING:\n\n")
             file.write("Recorded Time Of Yur Shopping Is:\n")
             file.write(f"{current_time}\n")
             file.write("\n")
             file.write("Products Details:\n")
             file.write("\n")
             for check in user_list:
              for key,value in check.items():
                file.write(f"{key} {value}\n")
             file.write(f"Total Bill Is {bill} Rs\n")
             file.write("\n")
             file.seek(0)     # seek to move cursor to start
             print("\n\n\t\t\t** COMPUTER ZONE **")
             print("\t\t\t    Invoice / Bill\n")
             print(f"Total Bill Is {bill} Rs")
             print()
             print("THANK YOU For Shopping with COMPUTER ZONE!! ")
             print()
             print("Catch you later! The application is heading out.")
             print()
             # Writing to the file
             with open(file_admin, "w+") as file:
                for every in menu_list:
                  line = separated.join([f"{key}{separated}{value}" for key, value in every.items()])
                  file.write(f"{line}\n")
             exit()      # use exit to end immediately
         elif ask_by_user=="no":
          print("Alright!! Do Some More Shopping")
          print("Computer Zone always here to serves you!")
          
          return     # return to market choices
         else:
          print("Please Enter Correct Word (yes/no)")


# user history function
def see_history(menu_list,user_list,file_market):
    try:   # use try except to avoid crush
     with open(file_market) as file:
      contents=file.read()
      print(contents)         # open user file  to show his history
    except(FileNotFoundError):
       print("Welcome to our store! As a first-time visitor, you currently don't have a purchase history")
       print("Come Back Later After Do Some Shopping")
       print()
       print()

