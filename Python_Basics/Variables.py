number=4000 #This is a variable containing intergers
float = 700.82 #This is a variable containing float numbers
string = "Jerome" #This is a variable containing a string

id(number)
id(float) #Provides the stored data location 

del float #Deleted the float variable
print (number)
print(float)
print (string)

print (type(number)) #prints out the type of variable "number" is

a=10
b=10
c=10 
#Is the same as
a=b=c=10

a,b,c = 10,20,30
print (a,b,c)

counter = 100
_count  = 100
name1 = "Zara"
name2 = "Nuha"
Age  = 20
zara_salary = 100000

print (counter)
print (_count)
print (name1)
print (name2)
print (Age)
print (zara_salary)  #Every variable in python should have a unique name. /
                        # See rules for variables at tutorialspoint.com/python/viarables.html

width = 10
height = 20
area = width*height
perimeter = 2*(width+height)
print ("Area = ", area)
print ("Perimeter = ", perimeter) #Once a variable has been allocated, it can be used multiple times

def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10))  #These are local variables where the variables are inputed at the level of the statement

def sum(x,y):
   sum = x + y
   return sum
print(sum(5, 10)) #Any variable created outside a function can be accessed with a function

a=b=10
a is b  #Pythons identity operator "is" returns true if both operands have same id() value
True
id(a), id(b)
