# 1️⃣ ZeroDivisionError

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# 2️⃣ ValueError
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Error: Please enter a valid integer")
