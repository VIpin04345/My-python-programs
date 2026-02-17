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
