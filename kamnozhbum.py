import random


choices = ["paper", "rock", "scissors"]
chosen = random.choice(choices)

n = input("Rock, paper, or scissors? ")
n = str(n)



lose = "You lose!"
win = "You win!"

print (f"Python Bot threw {chosen}, and you threw {n}!")
if n == chosen:
    print("We tied!")
elif n == "paper":
    if chosen == "rock":
        print(win)
    else:
        print(lose)
elif n == "rock":
    if chosen == "scissors":
        print(win)
    else:
        print(lose)
elif n == "scissors":
    if chosen == "paper":
        print(win)
    else:
        print(lose)
