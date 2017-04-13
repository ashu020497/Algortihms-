#Temp value
from sys import argv
x = int(argv[1])
y = int(argv[2])
print x,y
temp = x
x = y
y = temp
print x,y

#Multi-swap
x,y = y,x
print x,y

#Addition & Subtraction
x = x+y
y = x-y
x = x-y
print x,y

#Multiplication and Division
x = x*y
y = x/y
x = x/y
print x,y

#XOR
x = x^y
print x
y = x^y
print y
x = x^y
print x
