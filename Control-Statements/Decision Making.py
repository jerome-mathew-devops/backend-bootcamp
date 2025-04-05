#Single Statement
var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print ("Good bye!")

#If Else Statement
var = 100
if ( var == 100 ): 
   print ("Value of var is equal to 100")
else:
   print("Value of var is not equal to 100")

#Nest If Statementsvar = 100
if ( var == 100 ):
   print("The number is equal to 100")
   if var % 2 == 0:
      print("The number is even")
   else:
      print("The given number is odd")
elif var == 0:
   print("The given number is zero")
else:
   print("The given number is negative")
