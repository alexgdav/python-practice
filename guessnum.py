import random


chosen = random.randint(1, 20)

n = input("Guess what number between 1 & 20 I'm thinking of")
n = int(n)

if n == chosen:
    print(f"You got it, I'm thinking of {n}")
elif n > chosen:
    print(f"You guessed too high! I was thinking of {chosen}")
elif n < chosen:
    print(f"You guessed too low! I was thinking of {chosen}")
