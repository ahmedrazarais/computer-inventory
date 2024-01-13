from shared import file_name


def file_data_read(final):
    x = "@#$!"
    final.clear()  # Clear existing data before reading from file
    with open(file_name) as file:
        for line in file:
            data = line.strip().split(f"{x}")     #split on our seperator
            user_dic = {"username": data[0], "password": data[1], "passwordhint": data[2]}
            final.append(user_dic)    # append in final list


def search_any_account(final):
   file_data_read(final)  # Reload data after adding          
   fix="username"
   user_name_Ask=input("Enter User Name To Search Record:")
   has_found=False
   for every in final:
     if every.get(fix)==user_name_Ask:
       has_found=True
       if has_found:
          print()
          print(f'UserName: {every.get("username")}')
          print(f'Password: {every.get("password")}')
          print(f'PasswordHint: {every.get("passwordhint")}')
          print()
          print()
          break
       
def see_all_data(final):
    file_data_read(final)
    print("\tUSERS DETAILS")
    print()
    print(f"{"UsersNames"}:{"Passwords"}")
    print()
    for dic in final:
        for key,value in dic.items():
            print(f"{key} : {value}")
        print()

def delete_account(final):
    x="@#$!"
    user_name_to_delete = input("Enter User Name To Delete Record:").strip()

    with open(file_name, "r") as file:
        lines = file.readlines()

    new_lines = []  # Store modified lines here
    deleted = False  # Flag to track deletion
    for line in lines:
        data = line.strip().split(f"{x}")
        if data[0] != user_name_to_delete:
            new_lines.append(line)  # Keep lines for other usernames
        else:
            deleted = True
            print(f"Account for {user_name_to_delete} deleted successfully.")
    if not deleted:
       print("No Username Of That Name")
    with open(file_name, "w") as file:
        file.writelines(new_lines)  # Write back the modified lines

    # Update final list only if deletion occurred
    if deleted:
        final = [user for user in final if user["username"] != user_name_to_delete]
# delete_account(final)