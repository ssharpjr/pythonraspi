import random

secret = int(random.uniform(0,10))
print("I'm thinking of a number between zero and ten."
      , "can you guess what it is?")
guess = 11

while guess != secret:
    guess = int(input("Take a guess: "))

print("Well done!")
