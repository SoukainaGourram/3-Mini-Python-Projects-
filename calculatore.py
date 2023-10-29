# Function to add two numbers
def add(n1, n2):
    return n1 + n2

# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2

# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2 

# Function to divide two numbers
def divide(n1, n2):
    if n2 == 0:
        return "Impossible"
    return n1 / n2

print("Please select an operation:\n"
      "1: Add\n"
      "2: Subtract\n"
      "3: Multiply\n"
      "4: Divide\n")

select = int(input("Select operation from 1, 2, 3, 4: "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if select == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif select == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))
elif select == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif select == 4:
    result = divide(num1, num2)
    if result == "Impossible":
        print(result)
    else:
        print(num1, "/", num2, "=", result)
else:
    print("Invalid input")

