# 1.> write a program to add two numbers.

# (solution with predefine variables)
num1=30
num2= 40
sum=num1+num2
print('the sum of given number is',sum)


# (solution with user input)

num=float(input('enter a number '))
num2=float(input('enter another number'))
sum=num+num2
print('the sum of the provided to number is' , sum)
print('hello world')

# python program to find square root of a given number .


# (solution with exponentiation)

# num=81

num = int(input("enter a number:-"))
sr = num ** (1/2)  or (0.5)
print("the square root of the given number is ", sr)


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
for i in range(n, i - 1, -1):
    sum += i**3
    i += 1
print(sum)

# write a program to print only even number between 1 to n.


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



#   LIST   #


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

