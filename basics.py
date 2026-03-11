# 1.> write a program to add two numbers.

# (solution with predefine variables)
num1=30
num2= 40
sum=num1+num2
print('the sum of given number is',sum)


var1=int(input('enter a number'))
var2=int(input('enter a number'))
print('before swapping',var1,var2)
temp=var1
var1=var2
var2=temp
print('after sapping',var1,var2)
# (solution with user input)


num=float(input('enter a number '))
num2=float(input('enter another number'))
sum=num+num2
print('the sum of the provided to number is' , sum)
print('hello world')


num=float(input('enter a number '))
num2=float(input('enter another number'))
sum=num+num2
print('the sum of the provided to number is' , sum)
print('hello world')

# python program to find square root of a given number .
# num=81

num = int(input("enter a number:-"))
sr = num ** (1/2)  or (0.5)
print("the square root of the given number is ", sr)

# write a program to find area of ractangle
 
height=float(input('enter the hight of trangle'))
width=float(input('enter the width of the trangle'))
area=(1/2)*height*width
print('the area of ractangle is ',area)
# (solution using math module)

import math
num=int(input('enter a number :-'))
sr=math.sqrt(num)
print('the square root of the given number is',sr)


# write a program to find area of ractangle
 
height=float(input('enter the hight of trangle'))
width=float(input('enter the width of the trangle'))
area=(1/2)*height*width
print('the area of ractangle is ',area)


# write a program to find quadratic equation ax**2+bx+c=0
# whare, a ,  and c are the real numbers
# a!=0
import cmath
a=int(input('enter a number(a!=0):-'))
b=int(input('enter a number:-'))
c=int(input('enter a number:-'))
d=(b**2 )- (4*a*c)
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print('the roots are ',root1,root2)


# write a program to swap two variables.

var1=int(input('enter a number'))
var2=int(input('enter a number'))
print('before swapping',var1,var2)
temp=var1
var1=var2
var2=temp
print('after sapping',var1,var2)


# without using third variables

x=12
y=13
x,y=y,x
print(x,y)


# write a program to generate random number


import random
number=random.randint(1000,9999)
print(number)


# write a program to print from 1 to 10.

i = 1
while i <= 10:
    print(i)
    i += 1
print()

for i in range(1, 11):
    print(i)
print()

# write a program to print from 1 to n.

n = int(input("enter a number:-"))
i = 1
while i <= n:
    print(i)
    i += 1
print()


n = int(input("enter a number:-"))
for i in range(1, n + 1):
    print(i)
print()

n = int(input("enter a number:-"))
for i in range(1, n + 1):
    print(i)
print()




i = 10
while i >= 1:
    print(i)
    i -= 1
print()

for i in range(10, 1 - 1, -1):
    print(i)
print()

# write a program to print from n to 1.


n = int(input("enter a number:-"))
i = 1
while n >= i:
    print(n)
    n -= 1
print()
n = int(input("enter a number:-"))
for i in range(n, 0, -1):
    print(i)

# write a program to print sum of n to 1.

n = int(input("enter a number:-"))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i += 1
print(sum)


n = int(input("enter a number:-"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum = sum + i
print(sum)


n = int(input("enter your number:-"))
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i += 1
print(sum)

# write a program to print sum of squre of 1 to n natural numbers.


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**2
    i += 1
print(sum)


n = int(input("enter a number:"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum += i**2
    i += 1
print(sum)

# write a program to print sum of cube of 1 to n natural numbers.


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**3
    i += 1
print(sum)


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**3
    i += 1
print(sum)


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**3
    i += 1
print(sum)

n = int(input("enter a number:"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum += i**3
    i += 1
print(sum)

# write a program to print only even number between 1 to n.


n = int(input("enter a number:"))
sum = 0
i = 1
while i <= n:
    sum = sum + i**2
    i += 1
print(sum)


n = int(input("enter a number:"))
sum = 0
i = 1
for i in range(n, i - 1, -1):
    sum += i**2
    i += 1
print(sum)
n = int(input("enter a number:-"))
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


n = int(input("enter a number:-"))
i = 1
for i in range(i, n + 1):
    if i % 2 == 0:
        print(i)


# write a program to find sum of even number from 1 to n.

n = int(input("entera number:-"))
sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)



n = int(input("entera number:-"))
sum = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)


n = int(input("enter a number"))
sum = 0
i = 1
for i in range(i, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)


# write a program to find sum of first n even numbers.

n = int(input("enter  number :-"))
sum = 0
i = 1
while i <= n:
    if i % 2 != 0:
        sum = sum + i
    i += 1
print(sum)


str='shubham yadav'
print(str)

str='shubham yadav'
print(str[2])
print(str[10])

name='shubhamyadav'
print(name[1:6])

name='shubhamyadav'
print(name[:-1])

name='shubhamyyadav'
print(name[5])

name='shubhamyadav'
# print(name[3:])


this is shubham yadav
from the varanashi
he want to become a
software engineer to make his career better
he want to access all the apportunity which he want



this is shubham yadav
from the varanashi
he want to become a
software engineer to make his career better
he want to access all the apportunity which he want


str1='hello world'
str2='hello python'
print(str1==str2)


s='abcdef'
t='abcdef'
print(s==t)

a='adadada'
b='adadad'
c='adadada'
print(a==c)
print(a==b)


str1='hello world'
str2='hello python'
name=str1+str2
print(name)


a='py'
b='th'
c='on'
d=a+b+c
print(d)


name='hello world'
for o in name:
    print(o)


name='shubham yadav'
print(len(name))


str='hello world'
print(len(str))


name='Shubham yadav'
print(name.upper())

name='SHUBHAM YADAV'
print(name.lower())

str='shubham singh'
print(str.replace('singh','yadav'))


name='     shubham yadav      '
print(name.strip())

name='shUBhaM'
print(name.capitalize())



name='shUBhaM'
print(name.capitalize())

name='ShuBHam'
print(name.casefold())


name='shubham yadav computer science'
print(name.title())


name='shubham'
name1='YADAV'
print(name.isalpha())
print(name1.isalpha())

name='vipin8950'
print(name.isalpha())

name='shubham73737'
name1='VIPIN63637'
print(name.isalnum())
print(name1.isalnum())

str='4566'
print(str.isalnum())


str='shubham'
print(str.isnumeric())


str='2537585'
print(str.isnumeric())

name='SHUbham'
print(name.isupper())


name='SHUBHAM'
print(name.isupper())

str='shuBHam'
print(str.islower())

name='shubham73737'
name1='VIPIN63637'
print(name.isalnum())
print(name1.isalnum())

str='shubham'
print(str.islower())


str='shubham'
print(str.count('h'))

str='python is a popular programming language'
print(str.count('p'))

str='2345'
print(str.isdecimal())

str="shubham"
for i in str:
    print(i+&)

def first_non_repeating(s):
    for ch in s:
        if s.count(ch) == 1:
            return ch
    return None

# Test
string = "aabbcdde"
result = first_non_repeating(string)

if result:
    print("First non-repeating character is:", result)
else:
    print("No unique character found")

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Test
s1 = "listen"
s2 = "silent"




string = "aabbcdde"
result = first_non_repeating(string)

if result:
    print("First non-repeating character is:", result)
else:
    print("No unique character found")

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Test
s1 = "listen"
s2 = "silent"

print("Are Anagrams:", is_anagram(s1, s2))

#   LIST   #

def second_largest(lst):
    largest = second = float('-inf')
    
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second


def remove_duplicates(lst):
    unique = []
    
    for item in lst:
        if item not in unique:
            unique.append(item)
    
    return unique

# Test

numbers = [1, 2, 2, 3, 4, 3, 5]
print("After Removing Duplicates:", remove_duplicates(numbers))
# Test
numbers = [10, 20, 4, 45, 99]
print("Second Largest:", second_largest(numbers))

l1=['radha','krishna','ujala']
print(l1)

l1=['1','2','3','4']
for i in range(len(l1)):
    print(l1[i])


l2=['shubham','yadav','cse','3rd year']
for i in range(len(l2)):
    print(l2[i])


a=['1','2','3','4','5','6']
for j in range(len(a)):
    print(a[j])


l1=[1,2,3,4,5,6,]
del l1[2]
print(l1)

l1=[1,2,3,4,5,6]
l1.remove(3)
print(l1)




n = int(input("enter your first number:-"))
m = int(input("enter your second number:-"))
print("before swapping", n, m)
l = str(input("you are want to swap the value"))
v = "yes"
u = "no"
if l == v:
    n, m = m, n
    print("after swapping", n, m)

elif l == u:
    print("okay as your wish")
    n, m = n, m
    print("without swapping", n, m)

else:
    print("invalid command")




n = float(input("enter your marks in java:-"))
o = float(input("enter your marks in pyton:-"))
p = float(input("enter your marks in php:-"))
q = float(input("enter your marks in django:-"))
r = float(input("enter your marks in html:-"))
s = float(input("enter your marks in css:-"))
t = n + o + p + q + r + s
print("total percentage is ", t / 600 * 100)

# write a program to print the factorial of a given numbers.

n=int(input ('enter a number:-'))
fact=1
while n>0:
    fact*=n
    n-=1
print(fact)

# write a program to check weather the given program is prime or not.

n= int(input('enter a number:-'))
count=0
i=1
while(i<=n):
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print('prime')
else:
    print('not prime')


 # write a program to check weather the number is palindrom or not.
string = "aabbcdde"
result = first_non_repeating(string)

if result:
    print("First non-repeating character is:", result)
else:
    print("No unique character found")

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False

# Test
s1 = "listen"
s2 = "silent"


n=int(input('enter a number:-'))
rev=0
x=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
if x==rev:
    print('palin')
else:
    print('not palin')





 # write a program to check weather the number is palindrom or not

n=int(input('enter aa number:-'))
rev=0
x=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
    
if x==rev:
    print('palin')
else:
    print('not palin')

n= int(input('enter a number:-'))
count=0
i=1
while(i<=n):
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print('prime')
else:
    print('not prime')




#  write a program to find the fibonecci series

n=int(input('enter a number:-'))
x=0
y=1
z=0
while z<=n:
    print(z)
    x=y
    y=z
    z=x+y
    x+=1




 # write a program to reverse  a given numbers.

n=int(input('enter a number'))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print(rev)



 # write a program to find sum of even digit and prod of odd digit of a given number.
 
 
n=int(input('enter a number'))
sum=0
prod=1
while n>0:
    digit=n%10
    if n%2==0:
        sum+=digit
    else:
        prod*=digit
    n//=10
print(sum,prod)



# WRITE  A PROGRM TO CHECK WEATHER THE NUMBER IS ARMSTRONG OR NOT .

n=int(input('enter a number'))
sum=0
temp=n
len=len(str(n))
while n>0:
    digit=n%10
    sum+=digit**len
    n//=10
if temp==sum:
    print ('arm')
else:
    print('not arm')


# Function to find square of a number.

def sqaure(n):
    s=n**2
    print(s)
sqaure(9)

# Function to find factorial of a number.
def fact(n):
    facct=1
    while n>0:
        facct*=n
        n-=1
    return facct
print(fact(5))


# Function to reverse a string.

def rev(s):
    rev=''
    for i in s:
        rev=i+rev
    return rev
print(rev('shubham'))

# Function to check if string is palindrome.

def palin(p):
    rev=0
    x=p
    while p>0:
        digit=p%10
        rev=rev*10+digit
        p//=10
    if x==rev:
        print('palin')
    else:
        print('not')
palin(123219)

# Function to count vowels in a string.
str='shubhamOU'
count=0
for i in str:
    if  i in 'a e i o u A E I O U':
        count+=1
print('vowels is', count)

def vowels(str):
    count=0
    for i in str:
        if i in 'a e i o u  A E I O U':
            count+=1
    return count
print(vowels('shubhamUU'))



# Function to return max of three numbers.


def max_number(a, b, c):
    if a > b and a>c:
        print(a, "is max")
    elif b > a and b>c:
        print(b, "is max")
    else:
        print(c, "is max")

max_number(60, 50, 40)


str='aabbbbcdddrreeeggg'
freq={}
for i in str:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)  


# dictionary into the python.............


fees = {"anand": 2000, "shubham": 74200, "ajay": 300}
print(fees)
print(fees["shubham"])
for o in fees:
    print(o)






# modification of dictionary.........


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






# convert list into dictionary............


roll = [101, 102, 103]
name = ["akash", "vishal", "vipul"]
z = zip(roll, name)
d = dict(z)
print(d)
print(d[103])




# taking input from user(key , value)

a = {}
n = int(input("enter total number of element:-"))
for i in range(n):
    k = input("enter key")
    v = input("enter value")
    a.update({k: v})
print(a)



RANDOM MODULE 

import random model
from random import function name
or
import random



how to use random model.......



1> choice()
from random import choice
l1=[1,2,3,4,5,6,7]
print(choice(l1))






# 2> (randint())
from random import randint
otp=randint(1324,9786)
print(otp)


# 3> (suffle())

from random import shuffle
l1=['apple','banana','grapes','guvava']
shuffle(l1)
print(l1)




#       MATH MODULE


import math model
 import math
from math import function name

# how to use math module

# 1> (factorial())


import math 
print(math.factorial(4))


# 2> (ceil())

import math
print(math.ceil(4.56))


# 3> (floor())

import math
print(math.floor(3.2)) 

# 4> (sqrt())

import math
print(math.sqrt(10))

n = 3
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))


n = 5
for i in range(n):
    if i == 0 or i == n-1:
        print("*" * n)
    else:
        print("*" + " "*(n-2) + "*")

n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))

n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))


# EXCEPTION CREATING

a=int(input('enter a number'))
print("a",a)
# we got a wrong input by the user
print('bye')


a=int(input('enter the value of A:'))
b=int(input('enter the value of B:'))
c=a/b # axeception occure on runtime devisor by 0
print('answer',c)
print('bye')


#  NOW WE HAVE TO HANDLE THIS KIND OF THE EXCEPTION IN PYTHON


# WE USE TRY: BLOCK 
# the code which is written try block can be occure error at run time



#     SINGLE EXCEPTION HANDLING
try:
    
  a=int(input('enter the value of A:'))
  b=int(input('enter the value of B:'))
  c=a/b      # axeception occure on runtime devisor by 0
  print('answer',c)
except Exception as e:
  print("exception caught:", e)
print('bye')


#     MANY EXCEPTION HANDLING

try:
    print(x)
except NameError:
    print('variable is not define')
except:
    print('exception caught')    


#   HOE TO USE ELSE WITH EXCEPTION PART


try:
    print('hello')
except :
    print('something went wrong')
else:
    print('nothing went wrong')    


#  FINALLY BLOCK

# it is run compulsury if error occure or not


try:
    print('hello')
except :
    print('something went wrong')
finally:
    print('finaly block')

try:
    print(x)
except :
    print('something went wrong')
finally:
    print('finaly block')



# USER DEFINE EXCEPTION

class MyException(Exception):
    pass

c=25
if c>5:
    raise MyException('something went wrong')




1️⃣ Linear Search (Basic)
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
print(linear_search(arr, 30))



2️⃣ Binary Search (Sorted Array)
def binary_search(arr, key):
    low, high = 0, len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 40))


3️⃣ Recursive Binary Search
def binary_search_rec(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search_rec(arr, low, mid-1, key)
    else:
        return binary_search_rec(arr, mid+1, high, key)

arr = [5, 10, 15, 20]
print(binary_search_rec(arr, 0, len(arr)-1, 15))



# 4️⃣ Jump Search (Intermediate)
import math

def jump_search(arr, key):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n)-1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == key:
            return i
    return -1



# 5️⃣ Interpolation Search
def interpolation_search(arr, key):
    low, high = 0, len(arr)-1

    while low <= high and key >= arr[low] and key <= arr[high]:
        pos = low + ((key-arr[low])*(high-low))//(arr[high]-arr[low])

        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1




# 🔄 Sorting Algorithms (5 Programs)
# 1️⃣ Bubble Sort (Basic)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5,3,8,1]))

# 2️⃣ Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3️⃣ Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


# 👉 Small data me fast.

# 4️⃣ Merge Sort (Intermediate)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k]=left[i]; i+=1
            else:
                arr[k]=right[j]; j+=1
            k+=1

        while i<len(left):
            arr[k]=left[i]; i+=1; k+=1

        while j<len(right):
            arr[k]=right[j]; j+=1; k+=1

    return arr

# 5️⃣ Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([8,3,1,7,0,10,2]))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Rahul", 21)
s1.display()

# Class aur Object (Basic Example)
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"Car Brand: {self.brand}")
        print(f"Price: {self.price}")

c1 = Car("Toyota", 800000)
c1.show_details()

# Constructor aur Method Example
class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


# Inheritance Example
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def show_salary(self):
        print("Salary:", self.salary)

e1 = Employee("Amit", 50000)
e1.show()
e1.show_salary()


class Company:
    company_name = "TCS"   # class variable

    def __init__(self, employee_name):
        self.employee_name = employee_name

e1 = Company("Ravi")
e2 = Company("Neha")

print(e1.employee_name, "works at", Company.company_name)
print(e2.employee_name, "works at", Company.

# Encapsulation Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print("Balance:", acc.get_balance())

#  Polymorphism Example
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

for animal in (Dog(), Cat()):
    animal.sound()

# 6️⃣ Method Overriding
class Animal:
    def sound(self):
        print("Animal makes sound")

class Cow(Animal):
    def sound(self):
        print("Cow says Moo")

a = Cow()
a.sound()

# 7️⃣ Class Variable Example
class Company:
    company_name = "TCS"   # class variable

    def __init__(self, employee_name):
        self.employee_name = employee_name

e1 = Company("Ravi")
e2 = Company("Neha")

print(e1.employee_name, "works at", Company.company_name)
print(e2.employee_name, "works at", Company.company_name)


# 8️ Multiple Inheritance Example
class Father:
    def skills(self):
        print("Gardening")

class Mother:
    def skills(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()   # Father ka method call hoga (MRO rule)
