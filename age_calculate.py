"""This program calculates the user's age based on their year of birth"""
try:

    name = input('Please enter your name: ')
    birth_year = input('Please enter the year you were born: ')
    age = 2025 - int(birth_year)

    if age > 120 or age < 0:
        print('Please enter a valid birth year!')
    else:
        print(f'Hi {name}. You are {age} years old.')

except ValueError:
    print('Please enter a number, not text!')
