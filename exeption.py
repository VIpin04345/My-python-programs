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

# 🔟 Dictionary KeyError
try:
    d = {"name": "Shubh", "age": 21}
    print(d["city"])
except KeyError:
    print("Key not found in dictionary")



# 1️⃣1️⃣ Custom Exception Class
    
class InvalidPasswordError(Exception):
    pass

try:
    password = input("Enter password: ")
    if len(password) < 8:
        raise InvalidPasswordError("Password too short")
    print("Password accepted")
except InvalidPasswordError as e:
    print("Error:", e)
    
# 1️⃣2️⃣ Bank Withdrawal

class InsufficientBalance(Exception):
    pass

balance = 5000

try:
    amount = int(input("Enter withdrawal amount: "))
    if amount > balance:
        raise InsufficientBalance("Not enough balance")
    balance -= amount
    print("Remaining balance:", balance)
except InsufficientBalance as e:
    print("Error:", e)
    
# 1️⃣3️⃣ Retry Mechanism

correct = 10
for i in range(3):
    try:
        num = int(input("Guess number: "))
        if num != correct:
            raise ValueError("Wrong guess")
        print("Correct!")
        break
    except ValueError as e:
        print(e)
        
# 1️⃣4️⃣ Login System

class LoginError(Exception):
    pass

try:
    username = input("Username: ")
    password = input("Password: ")
    if username != "admin" or password != "1234":
        raise LoginError("Invalid credentials")
    print("Login successful")
except LoginError as e:
    print("Error:", e)

# 1️⃣5️⃣ Import Error

try:
    import nonexistingmodule
except ImportError:
    print("Module not found")
1️⃣6️⃣ Division List
lst = [10, 20, 0, 40]
for num in lst:
    try:
        print(100 / num)
    except ZeroDivisionError:
        print("Skipped division by zero")

# 1️⃣7️⃣ Empty File Check

try:
    with open("data.txt", "r") as f:
        content = f.read()
        if not content:
            raise Exception("File is empty")
        print(content)
except Exception as e:
    print("Error:", e)

# 1️⃣8️⃣ Age Validation Function

def validate_age(age):
    if age <= 0 or age >= 120:
        raise ValueError("Invalid age")
    return "Valid age"

try:
    print(validate_age(150))
except ValueError as e:
    print("Error:", e)


# 1️⃣9️⃣ ATM PIN System
    
class InvalidPIN(Exception):
    pass
correct_pin = "1234"
attempts = 0

while attempts < 3:
    try:
        pin = input("Enter PIN: ")
        if pin != correct_pin:
            attempts += 1
            raise InvalidPIN("Wrong PIN")
        print("Access granted")
        break
    except InvalidPIN as e:
        print(e)

if attempts == 3:
    print("Account blocked")
# 2️⃣0️⃣ API Simulation
import random

try:
    error = random.choice(["connection", "timeout", "none"])
    if error == "connection":
        raise ConnectionError("Connection failed")
    elif error == "timeout":
        raise TimeoutError("Request timed out")
    else:
        print("API call successful")
except ConnectionError as e:
    print("Error:", e)
except TimeoutError as e:
    print("Error:", e)
except Exception as e:
    print("General Error:", e)

