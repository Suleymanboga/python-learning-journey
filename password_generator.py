"""Password Generator
Generate random passwords of the desired length"""
import random
import string
try:
    password_length = int(input("Please enter the desired password length: "))
    password= ""
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(password_length):
        password += random.choice(all_chars)
    print("Password:", password)
except ValueError:
    print("Please enter a number")
