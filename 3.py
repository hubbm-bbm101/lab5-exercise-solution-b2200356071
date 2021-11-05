
import random
number = random.randint(0,100)
x = False

while x == False:
    guess =int(input("Try to guess a number: "))
    if guess < number:
        print("Increase your number.")
        x = False

    elif guess > number:
        print("Decrease your number.")
        x = False
    else:
        print("Your answer is correct.")
        x = True