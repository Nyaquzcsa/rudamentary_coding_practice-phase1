import random

secret_number = random.randint(1,6)
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess_number: "))
    guess_count ++1
    if guess == secret_number:
        print("You win")
        break
    else:
        print("Try again!!!")
        print(secret_number)
