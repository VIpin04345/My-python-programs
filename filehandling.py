# 🟢 1. Basic – File Create & Write
f = open("demo.txt", "w")
f.write("Hello, this is my first file handling program.")
f.close()

print("File created and data written.")

# 🟢 2. File Read Program


f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

# 🟢 3. Append Data (Add without delete)
f = open("demo.txt", "a")
f.write("\nThis line is appended.")
f.close()

print("Data appended.")

# 🟢 4. Read Line by Line
f = open("demo.txt", "r")

for line in f:
    print(line.strip())

f.close()



# 🟡 5. Using with (Best Practice)

# 👉 Automatically file close ho jata hai.

with open("demo.txt", "r") as f:
    print(f.read())



# 🟡 6. Count Words in File
with open("demo.txt", "r") as f:
    data = f.read()
    words = data.split()
    print("Total words:", len(words))



# 🟡 7. Copy File Content
with open("demo.txt", "r") as f1:
    with open("copy.txt", "w") as f2:
        f2.write(f1.read())

print("File copied successfully.")



# 🔵 8. File Exists Check
import os

if os.path.exists("demo.txt"):
    print("File exists")
else:
    print("File not found")


# -------------------------------------------------------------------------------------------------------

# 🟢  Count Specific Word in File
word_to_find = "Python"

with open("demo.txt", "r") as f:
    data = f.read()
    count = data.count(word_to_find)

print(f"'{word_to_find}' found {count} times.")


# 🟢  Replace Word in File
with open("demo.txt", "r") as f:
    data = f.read()

new_data = data.replace("Python", "Java")

with open("demo.txt", "w") as f:
    f.write(new_data)

print("Word replaced successfully.")

# 🟡  Count Uppercase & Lowercase Letters
with open("demo.txt", "r") as f:
    data = f.read()

upper = 0
lower = 0

for ch in data:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

# 🟡 Read First N Lines
n = 3

with open("demo.txt", "r") as f:
    for i in range(n):
        print(f.readline().strip())

# 🔵 Merge Two Files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    data1 = f1.read()
    data2 = f2.read()

with open("merged.txt", "w") as f:
    f.write(data1 + "\n" + data2)

print("Files merged successfully.")
