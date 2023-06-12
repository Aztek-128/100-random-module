#!python3
import random



num = random.randint(1,100)
guess = None

while guess != num:
    guess = input("enter a number from 1-100: ")
    guess = int(guess)
    if guess == num:
        print("congrats")
    elif guess < num:
        print("too low")
    elif guess > num:
        print("too high")
    else:
        print("ha, you lose")