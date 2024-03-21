from shared import file_name                #import text file from shared file
import os

final=[]
def first_name():  # amking function of last name first name address and email
    while True:
        last_name = input("Enter Your first Name:").strip()
         #applying several condition if user enter empty
        if not last_name:
            print("It Is Mandatory to fill this field")
        #allow only alphabets and spaces between
        elif not all(char.isalpha() or char.isspace() for char in last_name):
            print("Your Name Should Contain only alphabets")
        # checking not digits
        elif any(char.isdigit() for char in last_name):
            print("Your Name Should Not Contain Digits")
        #length must be greater than 3
        elif len(last_name) < 3:
            print("Your Name Is Too Short. Atleast Contain 3 Letters")
        else:
            break
def last_name():
    while True:
        first_name = input("Enter Your Last Name:").strip()
        #applying several condition if user enter empty
        if not first_name:
            print("It Is Mandatory to fill this field")
         #allow only alphabets and spaces between
        elif not all(char.isalpha() or char.isspace() for char in first_name):
            print("Your Name Should Contain only alphabets")
         # checking not digits
        elif any(char.isdigit() for char in first_name):
            print("Your Name Should Not Contain Digits")
          #length must be greater than 3
        elif len(first_name) < 3:
            print("Your Name Is Too Short.Atleast Contain 3 letters")
        else:
            break
        
def email():
    while True:

        #applying condition for emails
        email = input("Enter Your Email:")
        new_email=[char for char in email if char.strip()]
        if " " in email:
            print("Your Email Should Not Contain Spaces")
            
        elif '@' not in new_email:   
            print("Your Email Should Contain @ Symbol")
        
        elif '.' not in new_email:
            print("Your Email Should Contain . Symbol")
            
        elif 1<=len(new_email)<=4:
            print("Your Email is too Short")
                
        elif len(new_email)>4:
            break    
        else:
            print("It is mandatory to fill this field\nEnter your email again")
def address():
    while True:
     address = input("Enter Your address:")
     new_address=[char for char in address if char.strip()]
     #lehth of address must be greater than 2 
     if len(new_address)>2:
        break
     else:
        print("Address should have Atlesat Three Words")
        print("Enter Again")
        print()
#making a function signup in which every function we call
def signup(final):
    first_name()
    last_name()
    email()
    address()
    x = "@#$!" # our fix seperator
    # open accounts file
    with open(file_name) as file:
        for line in file:
            data = line.strip().split(f"{x}")
            user_dic = {"username": data[0], "password": data[1], "passwordhint": data[2]}
            final.append(user_dic)
 
    while True:
        # taking input of username
        user_name = input("Enter User Name Don't Contain Spaces: ")
        file_path = f"Database/UsersHistory/{user_name}.txt"
        # space not allowed
        if " " not in user_name and len(user_name) > 1:
            #checking that if username is already in list
            for check in final:
                if user_name.lower() == check["username"].lower() or os.path.exists(file_path):
                    print('Username is already taken. Please select another username.')
                    while True:
                    #asking for another chance
                     another_chance = input("Do you want another chance? (yes/no): ").lower()
                     if another_chance == "yes":
                        print("Alright Try Again!!")
                        break
                     elif another_chance =="no":
                        print("Back To Main Page")
                        return  # Exit the function if the user chooses not to try again
                     else:
                        print("Please Enter Correct Word Yes or no")
                        continue
                    break
            else:
                while True:
                    #taking input of password
                    password = input("Enter Your Password: ")
                    #applying condition for password strenth
                    if any(char.isdigit() for char in password) and any(not (char.isalnum()) for char in password) and len(password) >= 8:
                        while True:
                            password_hint = input("Enter Password Hint: ")
                            #open the file and write user data in file if it is not in file
                            with open(file_name, "a+") as file:
                                file.write(f"{user_name}{x}{password}{x}{password_hint}\n")
                                file.seek(0)

                                print("Signup Successful!")
                                return
                    else:
                        print("Password must contain at least 8 characters, at least 1 digit, and one or more special characters.")
        else:
            print("Username should not contain spaces. It is mandatory to fill this field.")
            while True:
             another_chance = input("Do you want another chance? (yes/no): ").lower()
             if another_chance =="yes":
                 print("Alright Try Again!")
                 print()
                 break
             elif another_chance=="no":
                print("Back To Main Page")
                return
             else:
                print("Please Enter Correct Word Yes Or No") # Exit the loop if the user chooses not to try again