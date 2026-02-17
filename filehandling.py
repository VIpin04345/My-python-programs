🟢 1. Basic – File Create & Write
f = open("demo.txt", "w")
f.write("Hello, this is my first file handling program.")
f.close()

print("File created and data written.")



🟢 2. File Read Program
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()



🟢 3. Append Data (Add without delete)
f = open("demo.txt", "a")
f.write("\nThis line is appended.")
f.close()

print("Data appended.")



🟢 4. Read Line by Line
f = open("demo.txt", "r")

for line in f:
    print(line.strip())

f.close()



🟡 5. Using with (Best Practice)

👉 Automatically file close ho jata hai.

with open("demo.txt", "r") as f:
    print(f.read())



🟡 6. Count Words in File
with open("demo.txt", "r") as f:
    data = f.read()
    words = data.split()
    print("Total words:", len(words))
