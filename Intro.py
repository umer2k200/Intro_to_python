#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#                      Some Built-in Functions
#int(),float(),string() for typecasting
#range() discussed below
#type(variable) gives the type of variable
#len(variable) gives you length of variable
#Math Functions:
#round(var) rounds the double value 
#abs(var) gives the absolute value means if + then + but if - then +
'''we can also use the math module like math library in c++
like this at the top of the file write : import math
then you can use anywhere in the program like math.tanh(var)
'''
#Proogram exited with code 0 means code has no errors
#Proogram exited with code 1 means code has errors
#there is another module which we use for our common tasks : standard library
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#(1)                          Comments
#for single line
#for multiple line comments you can do this
'''
like
this
'''
#you can also do this
"""
like
this
"""
#-----------------------------------------------------------------------
#(2)                      to print a anything
print("Hello World") #for single lines
#to print on next line, write this print() on next line
print('''Hello, 
My name is umer
and i am 20 years old''') #for multiple lines
#to print the value of a variable : print(variable)
#we can also do this

#to concatenate while printing : print("Hello"+ variable)
#to concatenate while printing : print("SUM = ",str(tno)) #here tno is integer variable
#we use this code : this is formatted string better than concatenation 
# message = f'Hi, my name is {course}'
#print(f'Hi, my name is {course}')
# print(message)
#-----------------------------------------------------------------------
#(3)                declaring and initializing variables
#no space b/w variable name
#name start by letter or underscore
#name cannot start with a number
#case sensitive
#name contain letters or numbers or underscores
#three types of data: numbers(integers+double),strings and booleans
age = 20
price = 19.25
my_name = 'umer'
father_name = "Zeeshan"
choice = True
#to print the value of the variable
print(age)
#-----------------------------------------------------------------------
#(4)                   Taking input from the user
#this will always return a string 
full_name = input("Enter your name : ")  
#additional(concatenating string):
print("Hello ", full_name)
#----------------------------------------------------------------------
#(5)                       Type Conversions
birth_year=input("Enter your birth year : ")
#age_2=2022-birth_year
#this above line will give an error because birt_year contains a string and 2022 is an integer
#now first we have to convert the string into an integer
age_2=2022 - int(birth_year)
print(age_2)
#int():to convert anything into an integer
#float(),bool(),str()
fno=input("Enter the first number : ")
sno=input("Enter the second number : ")
tno=float(fno)+float(sno)#to make even an int to float
print("SUM = ",str(tno)) #it concatenates only strings
#-----------------------------------------------------------------------
#(6)                    Strings & its operations                               
course="python for me"
#for example 
print(course.upper()) # to make upper case
print(course.lower()) # to make lower case
print(course)
print(course[0]) #gives first letter
print(course[-1]) #gives last letter and -2 for second last and so on
print(course[0:3]) #gives the sequence of characters between these indices,here from 0 to 2 : pyt
print(course[1:]) #ython for me
print(course[:5]) #pytho
another= course[:] #to make a clone/copy of the string course
print(another)
message = f'Hi, my name is {course}' #this is better than concatenation called formatted string
course = course.upper()
print(course) 
print(course.find('Y')) # to find a character or sequence of characters and gives its index
print(course.find('YTH'))
print(course.replace('Y','7')) #to find and then replace 
print(course.title()) #to capitalize the first letter of every word in the string
words= course.split(' ') #will split the string into words seperating with space
print(words)
print('PYTHON' in course) #only tells that this exist in variable or not by using in operator
#difference b/w find and in is find method gives the index and by in operator, we get a boolean answer
#-------------------------------------------------------------------------
#(7)                        Arithmetic operations
print(10+3)
print(10-3)
print(10*3) #for multiplication
print(10**3) #for exponent 10^3
print(10/3) #for floating answer
print(10//3) #for integer answer 
print(10%3) #for the remainder of the  division
x=10
x +=3 #augmented assignment operator 
#-------------------------------------------------------------------------
#(8)                       Operators Precedence
#first bracket,second exponentations, then d/m, then a/s rule 
#-------------------------------------------------------------------------
#(9)                       Comparison Operators
#==,>,<,>=,<=,!=
x= 3>2
print(x)
x= 3==2
print(x)
#-------------------------------------------------------------------------
#(10)                       Logical Operators
#and,or,not
price_2=25
print(price>10 and price <30) 
print(price>10 or price <30) 
print(not price>10) 
#-------------------------------------------------------------------------
#(11)                       If-else Statements
#in c++ we use curly braces to rep. block of code after if
#here we use indentation to rep.
temp=35
if temp >30 :
    print("Hot day!")
    print("Drink water")
elif temp>20 and temp<30:
    print("Nice DAy!")
else:
    print("Cold Day!")
print("Have a good day")
#More exercise
w=float(input("Weight: "))
ch=input("(K)g or (L)bs : " )
if  ch.upper()=='L':
    w/=2.205
    print("Weight in Kg: " + str(w))
elif ch.upper()=='K':
    w*=2.205
    print("Weight in Lbs: " + str(w))
else:
    print("Invalid Choice!")
#-------------------------------------------------------------------------
#(12)                          While loops
i=1
j=1
while i<=15:  #we can also do this i<=1_5
    print(i)
    i+=1
#now we know that we cannot concatenate a number with the string 
#means we cannot also concatenate a string with a number
#but we can multiply a string with a number
#so that the string will repeat based on that nummber
while j<=5:
    print(j*'Um')
    j+=1
#-------------------------------------------------------------------------
#(13)                            Lists
#like a list of objects
#some methods are same as of strings
names=["umer","ali",'ammar',"SAMMAD"]
print(names) # will print exactly same
print(names[0]) #will print the first element
print(names[3])  #last element
print(names[-1]) #last element
#now we can go till -3 if we start from last element and backwards
#we cannot go more than 2 if we start from first element
names[0]="UMER"
print(names[0:2])
#Find max in the list
#======================
# num=[1,4,3,7,12,3,45]
# max=num[0]
# for i in range(len(num)):
#     if num[i]>max:
#         max=num[i]
# print(f"Max is {max}")
#-------------------------------------------------------------------------
#                               2D Lists
_2dlist=[[1,2,3],[4,5,6],[7,8,9]]
print(_2dlist[0][1])
#-------------------------------------------------------------------------
#(14)                         Lists Methods
#len() gives the lenght of list and string
num=[1,2,3,4,5]
num.append(6) #add 6 after 5
num.insert(1,7) #first index and second value
num.remove(3)
num.pop() #pop the last element like stack
num.index(2) #gives the index of the value 2 in the list
num.clear() # clears all
num.sort() #sorts all the values in the lsit
num.copy() # returns a copy of the list
num.reverse() #reverses the list
print(1 in num)
print(len(num))
print(num)
#Program to remove the duplicates in a list
numberss=[1,4,3,7,4,12,3,45]
uniques=[]
for i in numberss:
    if i not in uniques:
        uniques.append(i)
print(uniques)

#-------------------------------------------------------------------------
#(15)                       For Loops
#Difference b/w for and while loops
#For loop
for k in num:
    print(k)
#While loop
l=0
while l<len(num):
    print(num[l])
    l+=1
#Nested for loops
for x in range(2):
    for y in range(3):
        print(f"({x},{y})")
#-------------------------------------------------------------------------
#(16)                       Range() Function
num_2= range(5)  #range object
print(num_2)
#  print(num_2)  #will give: range(0,5) #cuz it is a default rep.
#So we do this by for loop
for m in num_2:
    print(m)
num_3=range(5,10)
for n in num_3:
    print(n)
num_4=range(5,10,2)
for o in num_4:
    print(o)
#-------------------------------------------------------------------------
#(17)                         Tuples
#are like lists used to strore a sequence of objects
#but we cannot change them once we create them
#we dont have methods like list moethods
#we have count and index methods only
#in tuples we sorround them with small bracket instead of square bracket which we use for lists
num_5=(1,2,3,3)
print(num_5.count(3))
print(num_5.index(2))
#-------------------------------------------------------------------------
#(18)                         Unpacking
coordinates=[1,2,3]
#coordinates[0]*coordinates[1]*coordinates[2]
#it is very long so we do this:
#its alternative: 
#x=coordinates[0]
#y=coordinates[1]
#z=coordinates[2]
#which is this:
x,y,z=coordinates
print(x)
#-------------------------------------------------------------------------
#(19)                         Dictionaries
#we make dictionaries when we have to store a value of key pairs
#like if we want to add the data of the customers 
#so we know that the customer data is similar like name,email,phone etc
#common variables
customer={
    "name": "umer",
    "age" : 20,
    'isverified' : True
}
print(customer["name"])
#print(customer["AGE"])  this will give error cuz we dont have this in out dictionary
print(customer.get("AGE")) #this will give NONE but not an error
print(customer.get("AGE","2002"))# this will give 2002 instead of NONE
customer["name"] ="Ali" #update the key
customer["AGE"] = "2002" #will add new key
#EXAMPLE:
nums={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
}
inpp=input("Phone:")
outp=""
for i in inpp:
    outp+=nums[i]+" "
    #we can also do this
    #outp+= nums.get(i,"invalid")+" "
print(outp)
#Emojis Converter using dictionaries
emojis={
    ":)":"😊",
    ":(":"😔"
}
inp1=input("Type Good Morning :) OR Good Night :( : ")
wordss=inp1.split(" ")
out1=""
for k in wordss:
    out1+=emojis.get(k,k)
print(out1)
#-------------------------------------------------------------------------
#(20)                         Funcitons
#always call functions after its definition
#function without parameters
def greet_user():
    print("hello there")
    print("welcome")
print("end")
greet_user()
#function with parameters
def greet_user2(fname,sname):
     print(f"hello there {fname} {sname}")
greet_user2("Umer","Zeeshan")
print("end")
#------------------
#Keyword arguements:
#-------------------
#like in the above function umer goes to fname and zeeshan goes to sname
#just like the sequence of the above function's parameters
#but we can also do this by giving it a sequqence from us.
print("start")
greet_user2(sname="zeeshan",fname="umer")
print("end")
#now this is not the sequnce according to the parameters but
#but the value is set to fname and sname
#also
greet_user2("Umer","zeeshan")
greet_user2(sname="Umer",fname="zeeshan")
#greet_user2(fname="Umer","zeeshan") #these two will give error
#greet_user2("Umer",fname="zeeshan")
greet_user2("Umer",sname="zeeshan")
#-----------------
#function with return statement:
#-----------------
def add(fone,stwo):
    return fone+stwo
val=add(1,4)
print(val )
print(add(1,3))
#now when we dont use the return statement it will return "None"
#-------------------------------------------------------------------------
#(21)                    Exceptions          
# age_1 = int(input("Enter your age: "))
# print(age_1)
#-------------
#now this is for integer only
#what if the user enter other than integer
#thats why we use exceptions to handle the crash
#look the name of the error in the terminal
#here it is ValueError, so
try:
    age_1 = int(input("Enter your age: "))
    income = 3000
    risk = income/age_1
    print(age_1)
except ZeroDivisionError: #tis is if zero(age) comes below fraction
    print("age cannot be zero")
except ValueError: #if the value is not an integer
    print("Invalid value")
#-------------------------------------------------------------------------
#(22)                    Classes  
#we write "self" as a parameter in the methods of classes
#Classes without constructors
class point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
#we make methods inside the class
#here we are making variables outside the class when we create it's object
#like below
obj = point()
obj.x=10
obj.y=20 #now this object has two variable x and y
print(obj.x)
obj.draw()
obj.move()
z=obj.x +obj.y
#z=obj.x +obj.y + obj.f  #error becuase ther is no variable f
print(z)
obj2=point()
#-------------------------
#Classes with construcotrs
#-------------------------
#print(obj2.x) this line will also give error because now we
#have not make a variable x of this object
#to solve this we make constructors;called at the time of creating object
class point_2:
    def __init__(self,x,y):  #this is our constructor
        self.x=x
        self.y=y
pobj=point_2(10,20)
print(pobj.x)   #now ny constructor we have x and y variables of pobj object
#one more example :
class Person:
    def __init__(self,name):
        self.name=name
    def Talk(self): 
        print("The person is talking")
    def showname(self):
        print(f"Your name is {self.name}")
person_obj=Person("Umer")
person_obj.Talk()
person_obj.showname()
#-------------------------
#Classes with Inheritance
#-------------------------
# class Dog:
#     def walk(self):
#         print("walk")
# class Cat:
#     def walk(self):
#         print("walk") 
#now we have two walk functions same name
#it might make any problem in the future
#so thats why we use inheritance so both of the classes will
#inherit the walk function from a parent class
class mammal:
    def walk(self):
        print("walking")
class dog(mammal):  #we can also write any other functions of dog like bark() in this dog class but on the place of pass
    pass
class cat(mammal):
    def meow(self):
        print("meow")
m=mammal()
d=dog()
c=cat()
m.walk()
d.walk()
c.walk()
c.meow()
#-------------------------------------------------------------------------
#(23)                    Modules  
'''we can also use the math module like math library in c++
like this at the top of the file write : import math
then you can use anywhere in the program like math.tanh(var)
'''
#basically it is a file of some code
#we use modules to organize our code
# we can reuse the code
#when you make module,its better not to print or do anything
#outside the classes or functions,dictioantires or list methods
#so always write classes and functions and dictionaries and lists
import convertermodule
print(convertermodule.lbsintokg(132))
print(convertermodule.kgintolbs(59.4))
#there is also one other way to import the module
#in this way we can only import a particular class or fucntion
#instead of importing the whole module like
from convertermodule import kgintolbs
print(kgintolbs(59.4))
#we can also make an alias to make easy
import queue as q
#-------------------------------------------------------------------------
#(24)                    Packages  
#it is a directory or a folder
#it is a container for multiple modules 
#we add packages in the prjoect folder
#for example we have a mall, we call it a project
#in mall we have different sections like mens,womens and kids
#we call these sections as different packages
#now in men's section we have different things like 
#shoes,clothes for men
#now these things are different modules realted to current package
'''now here we cannot make a package cuz here we have not made a project
so whenever we make a project then we can right click on the project
and makea new directory eg we name it vehicle.
now this directory or  package vehicle has many modules like
car,bike etc and eg in car module we have car functions .
so now if we want to import the module of car from the vehicle package 
to our main file in our current project then we write:
import vehicle.car
and then we can use the functions of car module placed in the vehicle package
like: vehicle.car.move()
or by second method like
from vehicle.car import move
move()
OR if we have more functions then
from vehicle.car import move,stop,start
move()
start()
we can also do this like
from vehicle import car
car.move()
no we'll have all of the fucntions of the car module
'''
#-------------------------------------------------------------------------
#(25)                    Random values
import random
for i in range(3):
    print(random.random())
#if we have a range
for i in range(3):
    print(random.randint(10,20))
#if we have a list
list_mem=[45,32,77,121,44,12]
for i in range(3):
    print(random.choice(list_mem))
#random rolling of dice
class Dice:
    def roll(self):
        xind=random.randint(0,6)
        yind=random.randint(0,6)
        dtuple=(xind,yind)
        return dtuple
dice_obj=Dice()
dtuple_2=dice_obj.roll()
print(f"({dtuple_2[0]},{dtuple_2[1]})")
#-------------------------------------------------------------------------
#(26)                    Directories
from pathlib import Path
#two types of path 
#absolute path: eg c:\Program Files\Microsoft in windows
#                 /user/local/bin in macos
#we start from root
#relative path: this path exist in our current directory
#here we have not made a directory so suppose we have a direcotry called car
#now if we work with the relative path then
pathvar=Path("Intro")
print(pathvar.exists())
pathvar_2=Path("Bike")
#pathvar_2.mkdir() #will make the dierctory
#here we have already made the bike directory
print(pathvar_2.exists())
#we can also remove the diercotry by
#pathvar_2.rmdir()
#now if we want to see all the files in our directory then
pathvar_3=Path() #path of current directory
#print(pathvar_3.exists())
for i in pathvar_3.glob('*.py'): #searching for all py files
    print(i)
print("---------------")
for i in pathvar_3.glob('*'): #working for all files
    print(i)
#-------------------------------------------------------------------------
#(27)                    File I/O
#There are two types of files text and binary files (.dat,.jpg)
#Methods of opeing a file: 
'''r - open for reading
   w - open for writing
   a - open for appending
   + - open for updating
   rb- open for read in binary mode
   rt- open for read in text file mode '''
#------------------------------------------
#Writing a file:
#------------------------------------------
#when weopen a file for writing then
#it will open the file first of that name and then write teh string or something
#but if the file doesn't exist then it will create the file of that name first
# and then write the something
f=open ("mybio.txt",'w')
f.write("my name is umer. ")
f.close()
#now whenever we write something it overwrites
#but what if we dont want to overwrite anything
#then we will do this by append mode
#this will append,everytime we write
f=open("mybio.txt",'a')
f.write("I'm 21 years old. ")
f.close()
#------------------------------------------
#Opening a file:
#------------------------------------------
#when we open a file for reading then
#if the file does't exist then it will give error
#if the file exist then it will open without any problem
   #f=open("mybio.txt",'r') #first name then mode, here opeing file in read mode
#------------------------------------------
#reading a file:
#------------------------------------------
#now here it will not give any error because the file already exists.
#if we dont write r as read mode then default is also read mode
f= open("mybio.txt",'r')
#(1) text = f.read()  #to read its contents
# print(text)
#(2) text=f.read(4)
# print(text)
#(3) text= f.readline()
# print(text)
f.close()
#------------------------------------------
#Open and close the file automatically:
#------------------------------------------
with open("mybio.txt") as f:
    txt= f.read()
    print(txt)
#the file will close automatically