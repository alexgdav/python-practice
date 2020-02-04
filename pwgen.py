# import random to generate random selection
import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!?@#$%&()_+=~"

# check how many pws to generate, convert input to integer
number = input('Generate how many passwords?')
number = int(number)

# check for length of pw(s) to generate, convert input to integer
length = input('Generate password of what length?')
length = int(length)

# use the inputs to generate pw(s) - for each of the counts, generate a pw
# for each of the indexes in the length, add a random char from the characters string

for pwcount in range(number):
    password = ''
    for lengthcount in range(length):
        password += random.choice(characters)
    print(password)
