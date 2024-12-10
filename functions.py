                          #FUNCTIONS IN PYTHON

def ysh():
    print("hello")
     
ysh()
def greet(name):
    print("hey, "+name+".Good Morning!")
name="ysh"
greet(name)

def hello():
    a=5
    print("value of a:",a)
    print("\n")
    
    
    
a=10
hello()
print("a value is:",a)

name="ysh"
print(len(name))

#String functions

S="hello friends,how are you?"
if "are" in S:
    print("yes!!")

print("no!")
    
def name(name):
    print("hii, " + name + " how are you?")
    
name("padma")

#length of a string
n="123"
print(len(n))

#sorting a list

vowels=['a','i','o','e','u']
vowels.sort(reverse=True)
print("vowels are:",vowels)

#Appendinf an element to the list
list=[1,2,4,'easy',0.8,True]
list.append('False')
print(list)

li=[]
li.append('jasmine')
print(li)

#Nested functions/inner functions

def vehicle():
    print("ysh")
    def car():
        print("car have 4 wheels")
    car()
vehicle()



#Lamda functions

'''
x=3
def triple_function(x):
    return x*3

print(triple_function(5))
'''
triple_fun=lambda x: x + 6
print(triple_fun(5))

#Math functions

import math
print(math.sqrt(25))
print(math.sqrt(9))


#Exponential function
print(pow(6,8))#6 power 8

#reccursion functions

def factorial(x):
    if x==1:
        return 1
    else:
        return (x * factorial(x-1))
number=8
print("the factorial of ", number,"is:",factorial(number))
    

print(factorial(5))

#Not a pure function

def cut(y):
    del y[1]
    return y
def print1():
    a=[1,2,3]
    b=cut(a)
    print(b)
    print(a)
print1()

#pure function

def pure(a):
    return a[1:]
def calling():
    a=[1,2,3,4]
    b=pure(a)
    print(b)
    print(a)
calling()


#boolean function

print(13>4)


a=17
b="ysh"
c=0
sample=[]
n=""
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(sample))
print(bool(n))
