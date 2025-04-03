x=1          #Interger
y=True      #Boolean
z=10.82    #Float
t=10-6j   #complex

print (type(t))

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

tuple = "Python", 45, 67.9, 63, 6+3j #Data types not put in a bracket and seperated by commars, are treated as tuples

print (tuple)

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple because we attempted to update the values of a tuple
list[2] = 1000     # Valid syntax with list because a list mutable and update its content

for i in range(5):
  print(i)

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))

# Getting type of values
print(type(123))
print(type(9.99))

# Getting type of variables
a = 10
b = 2.12
c = "Hello"
d = (10, 20, 30)
e = [10, 20, 30]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Declaring a variable
# And, assigning an integer value

x = 10

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))

# Now, assigning string value to
# the same variable
x = "Hello World!"

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))


print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int(3.3)   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
#a = str(1)     # a will be "1" 
#b = str(2.2)   # b will be "2.2"
#c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)