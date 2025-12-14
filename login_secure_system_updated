"""Brute force login secure system v2.0"""

USER_NAME = "admin"
PASSWORD = "12345"
LOGIN_LIMIT = 3
login_count = 0

while login_count < LOGIN_LIMIT:
    login_count += 1
    
    remaining_attempts = LOGIN_LIMIT - login_count
    
    print(f"\n--- Attempt {login_count}/{LOGIN_LIMIT} ---")
    input_user = input("Username: ")
    input_pass = input("Password: ")

    if input_user == USER_NAME and input_pass == PASSWORD:
        print("\n>>> LOGIN SUCCESSFUL! Welcome.")
        break
    
    if len(input_user) <= 3 or len(input_pass) <= 3:
        print("Warning: Credentials are too short to be valid.")
    else:
        print("Error: Wrong username or password.")

    if remaining_attempts > 0:
        print(f"Please try again. You have {remaining_attempts} attempts left.")

else:
    print("\n!!! SYSTEM LOCKED !!! Too many wrong attempts.")
