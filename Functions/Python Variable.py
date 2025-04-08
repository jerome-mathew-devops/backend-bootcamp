def myfunction():
   a = 10
   b = 20
   print("variable a:", a)
   print("variable b:", b)
   return a+b
   
print (myfunction())

#global variables
name = 'TutorialsPoint'
marks = 50
def myfunction():
   # accessing inside the function
   print("name:", name)
   print("marks:", marks)
# function call   
myfunction()

def yourfunction():
   a = 5
   b = 6 
   # nested function
   def myfunction():
      # nonlocal function 
      nonlocal a
      nonlocal b
      a = 10
      b = 20 
      print("variable a:", a)
      print("variable b:", b)
      return a+b
   print (myfunction())
yourfunction()

def yourfunction():
   a = 5
   b = 6 
   # nested function
   def myfunction():
      # nonlocal function 
      nonlocal a
      nonlocal b
      a = 10
      b = 20 
      print("variable a:", a)
      print("variable b:", b)
      return a+b
   print (myfunction())
yourfunction()

name = 'TutorialsPoint'
marks = 50
result = True
def myfunction():
   a = 10
   b = 20
   return a+b
   
print (globals())

name = 'TutorialsPoint'
marks = 50
result = True
def myfunction():
   a = 10
   b = 20
   c = a+b
   print ("The value of c is:", c)
   print ("globals():", globals())
   print ("locals():", locals())
   return c
myfunction()

var1 = 50 # this is a global variable
var2 = 60 # this is a global variable
def myfunction():
   "Change values of global variables"
   globals()['var1'] = globals()['var1']+10
   global var2
   var2 = var2 + 20

myfunction()
print ("var1:",var1, "var2:",var2) #shows global variables with changed values