"""Brute force login secure system v1.0"""
USER_NAME = "admin"
PASSWORD = "12345"
LOGIN_COUNT = 0
LOGIN_LIMIT = 3

while LOGIN_COUNT < LOGIN_LIMIT:
    LOGIN_COUNT += 1
    login_user_name = input("User name: ")
    login_password = input("Password: ")
    if LOGIN_COUNT == LOGIN_LIMIT and len(login_password) <= 3 and len(login_user_name) <=3:
        print("Username and password are too short. Login failed.")
    elif LOGIN_COUNT == LOGIN_LIMIT and len(login_password) <= 3:
        print("The password is too short. Login failed.")
    elif LOGIN_COUNT == LOGIN_LIMIT and len(login_user_name) <=3:
        print("The username is too short. Login failed.")
    elif len(login_password) <= 3 and len(login_user_name) <=3:
        print("Username and password are too short. Please try again.")
    elif len(login_password) <= 3:
        print("The password is too short. Please try again.")
    elif len(login_user_name) <= 3:
        print("The username is too short. Please try again.")
    elif (USER_NAME != login_user_name or PASSWORD != login_password) and (LOGIN_COUNT != LOGIN_LIMIT):
        print("Wrong password or username! Please try again!")
    if login_user_name == USER_NAME and login_password == PASSWORD:
        print("Login successful")
        break
else:
    print("Too many wrong attempts. System locked.")
