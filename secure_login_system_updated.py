"""Brute force login secure system v2.0"""

USER_NAME = "admin"
PASSWORD = "12345"
LOGIN_LIMIT = 3
LOGIN_COUNT = 0

while LOGIN_COUNT < LOGIN_LIMIT:
    LOGIN_COUNT += 1
    REMAINING_ATTEMPTS = LOGIN_LIMIT - LOGIN_COUNT
    print(f"\n--- Attempt {LOGIN_COUNT}/{LOGIN_LIMIT} ---")
    input_user = input("Username: ")
    input_pass = input("Password: ")
    if input_user == USER_NAME and input_pass == PASSWORD:
        print("\n>>> LOGIN SUCCESSFUL! Welcome 0xSuleyman.")
        break
    if len(input_user) <= 3 or len(input_pass) <= 3:
        print("Warning: Credentials are too short to be valid.")
    else:
        print("Error: Wrong username or password.")
    if REMAINING_ATTEMPTS > 0:
        print(f"Please try again. You have {REMAINING_ATTEMPTS} attempts left.")
else:
    print("\n!!! SYSTEM LOCKED !!! Too many wrong attempts")
