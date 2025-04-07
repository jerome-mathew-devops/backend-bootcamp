def intr(amt, rate, /): #/ makes the function positional and a keyword arg will produce an error
   val = amt * rate / 100
   return val
   
print(intr(316200, 4)) 

def intr(amt, rate, /):
   val = amt * rate / 100
   return val
   
print(intr(amt=1000, rate=10))

def myfunction(x, /, y, *, z):
   print (x, y, z)
   
myfunction(10, y=20, z=30)
myfunction(10, 20, z=30)