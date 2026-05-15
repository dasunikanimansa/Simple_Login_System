user_data = {"username":"admin","password":"1234"}
count = 0
while True:
    entered_username = input("Enter the username: ")
    entered_password = input("Enter the password: ")
    if user_data["username"]== entered_username and user_data["password"]==entered_password:
        print("Login success!!")
        break
    else:
        print("Invalid username or password")
        count += 1
    if count == 3:
        print("Account locked")
        break
    
    