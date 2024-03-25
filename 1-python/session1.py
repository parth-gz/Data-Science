# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:37:13 2024

@author: gaikw
"""
###############################################################################
'''Session 2    15/03/2024'''
print ("hello world")
x=True
y=False
print(x+x)

###############################################################################
'''Session 3    19/03/2024'''
###############################################################################
        
a= None   #NoneType
print(type(a))
print(a is None) #is operator
print(a is not None) #is not operator

###############################################################################

num=int(input("Enter a number: "))
if num<0:
    print('num is negative')
elif num==0:
    print('num is zero')
else: 
    print('num is positive')
    
###############################################################################

savings=float(input("Enter savings: "))
if savings==0:
    print("Sorry no savings")
elif savings<500:
    print("Well done")
elif savings<1000:
    print("Thats a tidy sum")
elif savings<10000:
    print("Welcome sir!")
else:
    print("Thank you")
    
###############################################################################

count=0
print('starting')
while(count!=10):
    print(count)
    count +=1
###############################################################################
    
'''Session 4   20/03/2024'''

#odd numbers

start, end= 4, 19
for num in range(start, end+1):
    if num%2!=0:
        print(num, end=' ')
        
#even numbers

start, end= 4, 19
for num in range(start,end+1):
    if num%2==0:
        print(num, end=' ')
        
###############################################################################

#dictionary

X={"name":"Parth", "age":19}
print(type(X))
print(X["name"])
for i in X:
    print(X[i],end=' ')
print()
print(len(X))
print(X.keys())
print(X.values())

###############################################################################

#String

x="I am batman.I am vengeance."
print(x[:12])
print(x[12:])
print(x[::-1])
print(x[::-2])
print(x[-5:-1])
#palindrome

x=input("Enter name: ")
if x==x[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

###############################################################################

#strip function

x="   I am batman and I am vengeance."
print(x.strip())

#replace
print(type(x.replace("batman","spiderman").strip().split(' ')))

###############################################################################

print(x.find("and"))

x="I am batman."
y="I am vengeance."
print(x+" "+y)
###############################################################################

x=19
print(f"I am parth and I am {x} years old")

quantity=3
item_no=634
price=69
print(f"I want {quantity} pieces. Item number is {item_no}. price is {price}")
###############################################################################

'''Format method'''

my_order="I want {} pieces. Item number is {} and price is {}"
print(my_order.format(quantity,item_no,price))

my_order="I want {2} pieces. Item number is {0} and price is {1}"
print(my_order.format(item_no,price,quantity))

###############################################################################

#Escape character

print("My name is \"parth\"")  #with escape character
#print("My name is "parth"")  #without escape character

print(3**(3-2)/3*4+6)  

###############################################################################
'''LISTS
    properties:
    1. mutable
    2. allows duplicate values
    3. allows mixed data types'''
    
lst="cherry banana apple peach".split(' ')
print(lst)
print(len(lst))
lst.append("orange")
print(lst)
lst.extend("strawberry blueberry raspberry".split(' '))
print(lst)

#pop()
lst.pop(3)

#count()
print(lst.count("mango"))

#remove()
lst.remove("cherry")
lst.remove(3)
print(lst)

#sort()
lst.sort()
print(lst)

lst1=["red","blue","green"]
###############################################################################

'''TUPLE
    Properties:
    1.immutable
    2.allows mixed datatypes'''
    
tup=("cherry","apple","banana")
y=list(tup)
y[1]="kiwi"
x=tuple(y)
print(x)
z=tup+x
print(z)

###############################################################################

'''DICTIONARIES'''

dict={"brand":["Maruti","Mahindra","Toyota"],"model":['a','b','c'],"year":[2020,2021,2022]}
print(dict)
print(dict.keys())
print(dict.values())
dict.get("model")
dict1={"brand":"Ford","model":"Mustang","year":1990}
print(dict1)
dict1["color"]="yellow"
print(dict1)
dict1.get("brand")
print(dict1.items())
dict1
dict1.pop("year")
for x in dict1.values():
    print(x)
for x in dict1:
    print(x)
for key, value in dict1.items():
    print("%s=%s"%(key,value))

#copy

dict2=dict1.copy()
dict2

#Dictionary inside dictionary

myFamily={"child1":{"Name":"parth","Age":19},"child2":{"Name":"harsh","Age":18}}
myFamily
myFamily.clear()
x={"abc","def","ghi"}
y=0
dict1=dict.fromkeys(x,y)
dict1
dict1.get("abc")
print(dict1.get("abc"))
dict1.items()
dict1.values()
myFamily["child1"].update({"height":180})
myFamily
myFamily.replace("child2","child3")

###############################################################################

#control flow statements
lst

#break
for i in lst:
    print(i)
    if(i=="banana"):
        break

#continue
for i in lst:
    if(i=="banana"):
        continue
    print(i)
    
    
###############################################################################

#Range function

for x in range(2,30,3):
    print(x)
    
for x in lst1:
    for y in lst:
        print(x,y)
        
###############################################################################

#Functions

def add(a,b):
    c=a+b
    print("addition= ",c)
add(5,6)

###############################################################################

#Arbitrary arguments   (*args)

def myFunc(*name):
    print(name[1]+" "+name[3])
myFunc("hello","Hi","world","Parth")

###############################################################################

#Kwargs/keyword arguments (**kwargs)

def func1(**name):
    for key, value in name.items():
        print("%s= %s"%(key,value))
func1(first='Parth',mid='Somnath',last='Gaikwad')

#Function with default argument

def func(country="India"):
    print("I am from "+country)

func("Norway")  #if argument passed explicitly, it is used
func("Sweden")
func()          #if argument not passed explicitly, default argument (here, "India") is used

def func1(lst):
    for i in lst:
        print(i)
func1(lst)

###############################################################################

#function with return value

def fun(x):
    return x*x
print(f"Square of 5 is {fun(5)}")

###############################################################################

#Pass function

def fun():
    #print("hello")
    pass
fun()

###############################################################################


#Factorial of a number

def factorial(x):
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        return (x*factorial(x-1))
print(f"Factorial of 0 is {factorial(0)}")

###############################################################################

#Lambda fuction

#can have multiple arguments but only one expression
def add(a,b):
    return (a*b)/3
print(add(2,3))

#same as above
add=lambda a,b: (a*b)/3
print(add(2,3))

###############################################################################


odd_list=list(filter(lambda x:(x%2 !=0),lst))
print(odd_list)

#square numbers
lst=[1,2,3,4,5,6,7,8,9]
sqlst=[]
sqlst.extend(list(map(lambda x:x**2,lst)))
print(sqlst)

lst_sq=[]
for i in lst:
    lst_sq.append(i**2)
print(lst_sq)


a=lambda x:x*x
for x in lst:
    sqlst.append(a(x))
print(sqlst)

###############################################################################


print("Welcome to the roller coaster")
height=int(input("Please enter your height :"))
if height>=120:
    bill=0
    print("You are eligible for roller coaster !")
    
    
    age=int(input("Eneter your age in years :"))
  
    if age<=12:
        print("childs ticket is $5")
        bill+=10
    elif age>=18:
        print("Your ticket is $7")
        bill+=15
    elif age<=60:
        print("Your ticket is $10")
        bill+=20 
    else:
        print("As you are old you are not eligible ! ")
    print("Do you need popcorn ?")
    p=int(input("Enter 1 for popcorn :"))
    if p==1 :
        print("Enjoy your Popcorns ")
        bill+=5
        print(f"You need to pay {bill} ")
    else:
        print(f"You need to pay {bill}")
    print("Do you need photo ")
    Need_photo=(input("Enter Y or N :"))
    if Need_photo=='Y':
        bill+=3
        print(f"You need to pay {bill}")
    else:
        print(f"You you need to pay {bill}")
        
        
'''BMI calculator'''

Height=float(input("Enter your height in m :"))
Weight=float(input("Enter your weight in kg :"))
BMI=round((Weight/(Height*Height)),2)
if BMI <18.5:
    print(f"You are under weight and your BMI is{BMI} !")
elif BMI>18.5 and BMI<25 :
    print(f"you are normal weight and your BMI is {BMI} !")
elif BMI>25 and BMI<30:
    print(f"You are over weight and your BMI is {BMI} !")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is {BMI} !")
elif BMI>35:
    print(f"You are clinically obese and your BMI is {BMI} !")

#duplicates in list
lst1=[1,2,3,4,5,7,5,3]
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))


lst1=[1,2,3,4,5,5]
lst1.sort()
lst1
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))

###############################################################################

def is_leafyear(year):
    if((year>0) & ((year%4==0) &(year%100!=0))| ((year%400==0) & (year%100==0))):
        return True
    return False
if(is_leafyear(2024)):
    print("Leap year")
else:
    print("Not a leap year")
    

###############################################################################


#mario pyramid

for i in range(4):
    for j in range(i+1):
        print("#", end=" ")
    print()
    

for i in range(6):
    for j in range(i-1):
        print("#", end=" ")
    print()
    
    
#def diamond():
    
    
    
    
    
###############################################################################

#min max element

lst=[1,2,3,4,5,6,7,8,9]

def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    max = lst[0]
    for i in lst:
        if i>max:
            max=i
    print(f"min={min} and max= {max}")
min_max(lst)

###############################################################################

str=input("Enter: ")
if(str==str[::-1]):
    print("yes")
else:
    print("No")
    
users="admin employee manager worker staff".split(" ")
for user in users:
    user=input("Enter role: ")
    if user=="admin":
        print("Hello admin")
    elif user=="employee":
        print("hello employee")
    elif user=="manager":
        print("hello manager")
    elif user=="worker":
        print("hello worker")
    else:
        print("hello staff")
         
###############################################################################

