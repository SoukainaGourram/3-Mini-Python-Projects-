import random

user_range = input("Enter a number: ")
if user_range.isdigit():
    user_range = int(user_range)

    if user_range <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()
else:
    print("Please enter a valid number next time.")
    quit()

random_number = random.randint(0, user_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please try to enter a number.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess < random_number:
        print("You were below the number.")
    else:
        print("You were above the number.")

print("You got it in", guesses, "guesses.")
