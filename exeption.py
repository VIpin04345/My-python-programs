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


# 5️⃣ Finally Block
try:
    f = open("data.txt", "r")
    print(f.read())
except:
    print("Some error occurred")
finally:
    print("File operation completed")


# 6️⃣ Negative Age Validation
try:
    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age:", age)
except ValueError as e:
    print("Error:", e)

# 7️⃣ Raise for Voting
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise Exception("Not eligible to vote")
    print("Eligible to vote")
except Exception as e:
    print("Error:", e)

# 8️⃣ Nested Try
try:
    num = int(input("Enter number: "))
    try:
        result = 10 / num
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid input")


# 9️⃣ TypeError
def add(a, b):
    try:
        return a + b
    except TypeError:
        return "Both inputs must be numbers"

print(add(10, "5"))
