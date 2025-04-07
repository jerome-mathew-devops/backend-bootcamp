def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return;

# Now you can call the function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

def greet(name):
   print(f"Hello, {name}")

greet("Jerome")

def hello():
    name = str(input())
    print ("Hello my name is ", name)

hello()

def greetings(name):
   "This is docstring of greetings function"
   print ("Hello {}".format(name))
   return
   
greetings("Samay")
greetings("Pratima")
greetings("Steven")

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )

def posFun(x, y, /, z):
    print(x + y + z)

print("Evaluating positional-only arguments: ")
posFun(33, 22, z=11) 

def posFun(*, num1, num2, num3):
    print(num1 * num2 * num3)

print("Evaluating keyword-only arguments: ")
posFun(num1=6, num2=8, num3=5) 

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )

def add(x,y):
   z=x+y
   return z
a=10
b=20
result = add(a,b)
print ("a = {} b = {} a+b = {}".format(a, b, result))

