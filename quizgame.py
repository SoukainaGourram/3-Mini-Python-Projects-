print("Welcome to my quiz game")
answer = input("Do you want to play? ")
if answer.lower() != "yes":
    quit()

print("Okay, let's play!")
score = 0
# Q1
answer = input("Which keyword is used for a function in the Python language? ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q2
answer = input("To add a new element to a list, we use which Python command? ")
if answer.lower() == "list.append()":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q3
answer = input("Who developed the Python Programming Language? ")
if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# Q4
answer = input("Is Python case-sensitive when dealing with identifiers? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4)*100) + "%")
