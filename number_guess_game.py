"""Number guess game"""
try:
    import random
    random_number = random.randint(1, 100)
    guess = ""
    while guess != random_number:
        guess = int(input("Please enter a number between 1 and 100: "))
        if guess < random_number:
            print("Enter a larger number!")
        elif guess > random_number:
            print("Enter a smaller number!")
        else:
            print("Congratulations! Correct guess!")
            break
except ValueError:
    print("Please enter a number! Not a text!")
