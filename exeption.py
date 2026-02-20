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

# 3️⃣ Multiple Exceptions
try:
    lst = [10, 20, 30]
    index = int(input("Enter index: "))
    print(lst[index])
except ValueError:
    print("Invalid input! Enter integer index.")
except IndexError:
    print("Index out of range!")

# 4️⃣ FileNotFoundError
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
