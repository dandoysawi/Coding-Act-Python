import random

Secret_number = random.randint(1, 10)
guess = 0

while guess != Secret_number:
    guess = int(input("Guess a number between 1 - 10: "))

    if guess < 1 or guess > 10:
        print("Error! Please stay between 1-10 only")
    elif guess < Secret_number:
        print("Too low")
    elif guess > Secret_number:
        print("Too high")

# This runs only when guess == Secret_number
print("Correct!")
