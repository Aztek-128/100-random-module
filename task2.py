#!python3
import random





while True:
    which = random.choice["heads", "tails"]
    guess = input("heads or tails: ")
    if guess == which:
        print("you win")
    else:
        print("ha, you lose")