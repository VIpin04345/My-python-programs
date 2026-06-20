print("hello world")
print("python programs")
print("welcome to coding world")


a = 10
b = 20
c = a + b
print(c)


first = input("enter your choice")
second = input("enter your second choice")
print(first + second)


some = input("enter some value")
print("the value is ", some)
print(type(some))


year = 2024
dob = int(input("enter your dob"))
if dob <= year:
    print("your currunt age is ", year - dob)
else:
    print("please enter valid dob")


str = "my name is shubham "
z = "hellow guys how are you"
print(z)
print(str)


a = 10
print(a)
print(type(a))


a = "shubham"
print(a)
print(type(a))


a = 10.5
print(a)
print(type(a))


a = 3 + 4j
print(a)
print(type(a))


length = int(input("enter the length"))
breath = int(input("enter the breath"))
area = length * breath
print("area of ractangle is ", area)


num = int(input("enter the number"))
if num == 10:
    print("success")
print(" ")


first = int(input("enter your number"))
if first % 2 == 0:
    print("the number is divisible by 2")
else:
    print("the number is not divisible by 2")


first = int(input("please enter your first number"))
second = int(input("please enter your second number"))
if first > second:
    print("the first number is the gratest number")
elif first == second:
    print("both first and second number are equal")
else:
    print("the second number is the gratest number ")


a = 17
b = 16
if a > b:
    print("ram")
else:
    print("shyam")


num = int(input("please enter your number:"))
if num % 3 == 0:
    if num % 5:
        print("the number is divisible by both 3 and 5")
    else:
        print("the number is divisible by only 3")
else:
    if num % 5:
        print("the number is divisible by only 5")
    else:
        print("the number is not divisible by both 3 and 5")


day = int(input("please enter your number of day"))
if day == 1:
    print("today is the monday")
elif day == 2:
    print("today is the tuesday")
elif day == 3:
    print("today is the wednesday")
elif day == 4:
    print("today is the thirsday")
elif day == 5:
    print("today is the saturday")
else:
    print("today is the  sunday")


i = 5
while i <= 55:
    print(i)
    i += 1
print()


i = 1
while i <= 100:
    print(i)
    i += 1
print()


i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
print()


for i in range(1, 101):
    if i % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")


for i in range(0, 100 + 1):
    print(i)


for i in range(0, 100 + 1):
    if i % 2 == 0:
        print(i)


sum = 0
for i in range(1, 11):
    sum += i
else:
    print(sum)


i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
else:
    print(sum)


for i in range(1, 11):
    if i == 4:
        break
    print(i)
print()


for i in range(1, 50 + 1):
    if i == 45:
        break
    print(i)
print()


i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print()


for i in range(1,101,2):
    print(i)


for i in range(1, 11):
    if i == 3:
        continue
    print(i)
print()


for i in range(1, 51):
    if i == 10:
        continue
    print(i)
print()


for i in range(1, 11):
    if i == 2:
        pass
    print(i)
print()


strings in python..............


str = "python is a modern language"
print(str)


str1 = "python is a powerfull language"
print(str1)


str2 = "my name is john"
for i in str2:
    print(str2)


indexing in the strings.......


name = "shreya"
print(name[1])

name='shubham'
print(name[4])

slicing into the strings.....

name = "hello"
print(name[0:5])

name = "python"
print(name[0])
print(name[-1])
print(name[0:3])
print(name[-1:-4])


str1 = """python is a modern language
python is a powerfull language
python is a vast languag"""
print(str1)


x = """i am a coder
i am a programmer
i love coding
i love programming"""
print(x)


s = """a for apple
b for bucket
c for cricket
d for doll"""
print(s)


s1 = "hello world"
s2 = "hello python"
s3 = "hello world"
print(s1 == s2)
print(s1 == s3)


str1 = "hello"
str2 = " world"
str3 = "hello"
str4 = " python"
print(str1 + str2)
print(str3 + str4)


a = "py"
b = "th"
c = "on"
d = a + b + c
print(d)


name = "shubham"
for k in name:
    print(k)


strings built in function..........


str = "shubham yadav"
print(len(str))
print(str)


x = "my name is shubham yadav"
print(x.upper())


y='my name is shubham yadav'
print(y.lower())


name='hello john'
k=name.replace('john','shubham')
print(k)


name = "  hello john    "
print(name.strip())

name = "shubhahm"
print(name.capitalize())


name = "shubham yadav "
print(name.title())


str1='dilip123'
str2='shubahm'
print(str1.isalpha())
print(str2.isalpha())


str1='dilip'
str2='shubham123'
print(str1.isalnum())
print(str2.isalnum())


name = "shubham"
name2 = "SHUBAHM"
print(name.isupper())
print(name2.isupper())


name = "shubham"
name2 = "SHUBAHM"
print(name.islower())
print(name2.islower())


s = "python is a popular language"
# print(s.count("p"))

s='Hello'
print(s.casefold())


LISTS IN THE PYTHON.............


list = ["item1", "item2", "item3"]
print(list)


a = [10, 20, 30, 40, 2.4, 4.12, "india", "pak"]
for i in range(len(a)):
    print(a[i])


list = ["mango", "orange", "applle"]
for i in list:
    print(i)


a = [12, 3.4, 14, "ram", "shyam"]
for i in range(len(a)):
    print(a[i])


a = [10, 20, 3.4, "india", "ram"]
del a[2]
print(a)


list = ["shubham", "kishan", "mamata", "rajesh", "reeta"]
del list[0]
print(list)


a = [1, 2, 3, 4, 5, 6]
del a
print(a)

a = [12, 23, 54, 64, 75]
for i in range(len(a)):
    print(a[i])


a = ["rajesh", "reeta", "mamata", "kishan"]
a.append("shubham")
print(a)


n = [10, 20, 30, 40]
n.append(50)
for i in range(1, 4 + 1):
    print(n[i])


a = [10, 20, 3.4, "india"]
a.insert(2, 50)
print(a)


a = [12, 23, 5, 67, 5]
del a[1]
print(a)


name = ["rajesh", "reeta", "mamata", "kishan"]
name.insert(3, "shubham")
# print(name)
for i in range(0, 5):
    print(name[i])


a = [12, 13, 14, 15, 16]
a.pop()
print(a)


a = [12, 24, 125, 2.4, "shubham"]
a.remove("shubham")
print(a)


a = [12, 13, 14, 15, 16, 17, 18, 19, 20]
a.reverse()
print(a)
#


a = [13, 14, 1, 52, 4, 23, 234, 2, 24, 3]
a.clear()
print(a)


a = [12, 13, 145, 14, 24]
b = sum(a)
print(b)


a = [12, 24, 25, 254, 256]
b = [86, 96, 85, 869, 46, 26]
a.extend(b)
print(a)


a = ["ram", "kishan", "his", "her"]
b = [86, 96, 85, 869, 46, 26]
b.extend(a)
print(b)


a = [12, 13, 136, 514, 15, 1, 5, "shubham", "kishan"]
b = a.copy()
print(b)


a = [13, 242, 623, 63, 74, 85, 36, 36, 53, 6]
print(max(a))


a = [134, 5, 25, 235, 353, 63, 3, 74, 7, 3, 6]
print(min(a))


list slicing..............


a = [100, 101, 102, 103, 104]
print(a[1:4])


a = [100, 101, 102, 103, 104]
print(a[0])


a = [100, 101, 102, 103, 104]
print(a[-1])


a = [100, 101, 102, 103, 104]
print(a[0:5])


a = [100, 101, 102, 103, 104]
print(a[-1])


remaining operators.................

isoperator()

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
if a is b:
    print("equal")
else:
    print("not equal")


a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
if a is not b:
    print("equal")
else:
    print("not equal")


a = [1, 2, 3, 4, 5]
b = [9, 7, 5, 3, 0]
if a is b:
    print("ram")
else:
    print("shyam")


a = [1, 2, 3, 4, 5]
b = [0, 9, 8, 7, 6]
if a is not b:
    print("ram")
else:
    print("shyam")


a = [1, 2, 3, 4, 5]
if 3 in a:
    print("found")
else:
    print("not found")


a = [2, 4, 6, 7, 9, 5, 7]
if 21 in a:
    print("found")
else:
    print("not found")


b = [12, 1, 4, 234, 2454, 243, 34]
if 2 not in b:
    print("true")
else:
    print("not true")


b = [12, 1, 4, 234, 2454, 243, 34]
if 12 not in b:
    print("true")
else:
    print("not true")


tuples into the python................

t1 = (10, 20, -30, 23.24, "shubham", "india")
for i in t1:
    print(i)


t1 = (10, 20, -30, 23.24, "shubham", "india")
print(t1)


t1 = (13, 136, 25, 234, 16, 267)
print(t1[0:6])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[1])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[0])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[-1])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[-4:-1])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[1:])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[-1:])


t1 = (13, 136, 25, 234, 16, 267)
print(t1[:-1])


a = (12, 35, 68, 96, 35, 25, 65)
b = (123, 456, 789, 876, 543)
s = a + b
print(s)


a = ("shubham", "kishan")
b = ("ram", "shyam")
c = a + b
print(c)


a=(100,200,300,400,500,423,74,25,235,3)
print(sorted(a))


a = [12, 46, 354, 778, 45, 785]
print(sorted(a))


a = (12, 13, 14, 56, 78)
sum = sum(a)
print(sum)


t1 = (2, 3, 67, 47, 43, 745, 7)
st = tuple(sorted(t1, reverse=True))
print(st)


a = (12, 53, 64, 785, 85, 13)
sum = sum(a)
print(sum)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2)
print(len(a))


a = (1, 3, 65, 8, 5, 3, 6, 3, 7)
print(sorted(a))
print(tuple(reversed(a)))


a = ("india", "us", "uk")
print(tuple(reversed(a)))


a=(1,2,3,7,5,7,34,6,2,6,8,4,8,4,8,5)
# print(sorted(a))
t=tuple(sorted(a,reverse=True))
print(t)


t1 = ("apple", "mango", "guvava")
a = list(t1)
print(a)


a = ("apple", "mango", "guvava", "grapes")
x = list(a)
x.insert(1, "pineapple")
y = tuple(x)
print(y)


a = (11, 112, 1123, 11234)
b = (1, 2, 4, 6, 7)
print(a == b)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(a == b)


a = (1, 2, 3, 4)
b = (3, 4, 5, 6)
print(a != b)


a = (1, 2, 3, 4, 5, 6)
b = (1, 2, 3, 4, 5, 6)
print(a != b)


t1 = ("apple", "mango", "guvava", 1, 2, -4, 5)
i = 0
while i < len(t1):
    print(t1[i])
    i += 1


sets into the pythons..........


s1 = (10, 20, 30, "india", "python")
for k in s1:
    print(k)


s1 = {1, 2, 3, 4, 5, "shubham", "vip"}
print(s1)


a = {10, 20, 30, 40}
a.remove(30)
print(a)


s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, "shubham", "kishan"}
print(s1)
s1.remove("shubham")
print(s1)


s1 = {1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 9}
print(s1)
s1.remove(2)
print(s1)
for o in s1:
    print(o)


s1 = {1, 1, 2, 2, 3, 3, 4, 4, 5}
a = sum(s1)
print(a)


s1 = {1, 2, 3, 4, 5}
s1.add("shubham")
s1.add(23)
print(s1)


s1 = {1, 2, 3, 4, 5, 6, 7, 8}
s1.update([12, 13, 14, "shubham", "kishan"])
print(s1)


s1 = {12, 3, 45, 64, 4, 1, 24, 75, 24, 674, 66, 35, 25, 2, 0}
print(min(s1))


s1 = {1, 2, 54, 6, 8, 5, 2, 4, 85, 3, 65, 3, 6, 8, 433, 6, 4, 46}
print(max(s1))


s1 = {1, 2, 3, 4, 5, 6}
s2 = {9, 8, 7, 4, 2, 7, 3}
c = s1.union(s2)
print(c)


a = {11, 12, 13, 14}
b = {15, 16, 17, 18, "shubham"}
s = a.union(b)
# print(s)


a = {1, 2, 3, 4, 5}
b = {9, 8, 6, 4, 2}
n = a.intersection(b)
print(n)


a = {1, 2, 3, 4}
b = {2, 3, 7, 8, 9}
c = b.difference(a)
print(c)


a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 8, 9}
s = a.difference(b)
print(s)


a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
a.clear()
print(a)


b = {"shubhan", "kishan", "ram"}
b.clear()
print(b)


s = {1, 2, 4, 5, 7, 8, 9, 0}
s.copy()
print(s)


dictionary into the python.............


fees = {"anand": 2000, "shubham": 74200, "ajay": 300}
print(fees)
print(fees["shubham"])
for o in fees:
    print(o)


modification of dictionary............


k = {101: "rahul", 102: "anuj", 103: "akash"}
k[103] = "vishal"
print(k[103])
print(k)


k = {1: "ram", 2: "lakshman", 3: "bharat"}
k[104] = "satrughn"
print(k[104])


k = {1: "ram", 2: "bharat", 3: "vishal"}
del k[3]
print(k)


k = {1: "r", 2: "s", 3: "f"}
k.clear()
print(k)


k = {1: "a", 2: "b", 3: "c"}
k.copy()
print(k)


k = {1: "a", 2: "b", 3: "c", 4: "d"}
k.popitem()
print(k)


convert list into dictionary............


roll = [101, 102, 103]
name = ["akash", "vishal", "vipul"]
z = zip(roll, name)
d = dict(z)
print(d)
print(d[103])


taking input from user(key , value)

a = {}
n = int(input("enter total number of element:-"))
for i in range(n):
    k = input("enter key")
    v = input("enter value")
    a.update({k: v})
print(a)


k = {1: "ram", 2: "shyam", 3: "anuj"}
for i in k:
    print(k[i])


k = {1: "ram", 2: "shyam", 3: "anuj"}
for i in k:
    print(i)


k = {1: "ram", 2: "shyam", 3: "anuj"}
a = k.keys()
print(a)


k = {1: "ram", 2: "shyam", 3: "anuj"}
a = k.values()
print(a)


access the dictionary.............

d1 = {1: "apple", 2: "mango", 3: "guvava", 4: "grapes", "a": "b", "c": 4}
print(d1)
print(type(d1))


d1 = {
    1: "apple",
    2: "mango",
    3: "guvava",
    4: "grapes",
    "a": "b",
    "c": 4,
    "k": [1, 2, 3, 4, 5, "shubham", "kishan"],
}
print(d1["k"])


d1 = {1: "a", 2: "b", 3: "c", 4: ("bag", "pen", "pencil")}
print(d1[4])
for a in d1:
    print(d1[4])


access the value of dictinary...........


d1 = {1: "apple", 2: "grapes", 3: "mango", "a": "b"}
x = d1[3]
print(x)
y = d1.get("a")
print(y)


d1 = {1: "apple", 2: "grapes", 3: "mango", "a": "b"}
z = d1.items()
print(z)


d1 = {1: "apple", 2: "grapes", 3: "mango", "a": "b"}
d1[3] = "pineaaple"
print(d1[3])


d1 = {1: "apple", 2: "grapes", 3: "mango", "a": "b"}
d1["n"] = 10000
print(d1["n"])


d1 = {1: "apple", 2: "grapes", 3: "mango", "a": "b"}
d1.pop(3)
print(d1)




a=10
b=20
c=a-b
print(c)
