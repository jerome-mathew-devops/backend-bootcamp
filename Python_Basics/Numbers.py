a = 10
b = 20
c = a + b

print ("a:", a, "type:", type(a))
print ("c:", c, "type:", type(c))

a=float(16.7)
print (int(a))

a=0b101 #Binary number starts with 0b
print ("a:",a, "type:",type(a))

b=int("0b101011", 2) #the 0b101011 is the binary number and 2 is the base number
print ("b:",b, "type:",type(b))

a=43
b=bin(a)
print ("Integer:",a, "Binary equivalent:",b)

a=0o107 #Octal number. starts from 0-7 and must begin with 0o
print (a, type(a))

a=int('20',8) #The octal number is 20 and its base 7. Using int() function, to convert octal to string
#we use base 8
print (a, type(a))

a=0O56
print ("a:",a, "type:",type(a))

b=int("0O31",8)
print ("b:",b, "type:",type(b))

c=a+b
print ("addition:", c)

a=oct(71) #Octal string of an interger
print (a, type(a))

a=0XA2  #Its prefix is 0x
print (a, type(a))

a=int('0X1e', 16) #To set hexadecimal string to interger, we use base 16
print (a, type(a))

num_string = "A1"
number = int(num_string, 16)
print ("Hexadecimal:", num_string, "Integer:",number)

a=hex(161) #To get the hexadecimal equivalent of an interger
print (a, type(a))

a=10 #decimal
b=0b10 #binary
c=0O10 #octal
d=0XA #Hexadecimal
e=a+b+c+d

print ("addition:", e)

a=float(0b10)
b=float(0O10)
c=float(0xA)

print (a,b,c, sep=",")

a=float("-123.54")
b=float("1.23E04")
print ("a=",a,"b=",b)

a=complex(5.3,6)
b=complex(1.01E-2, 2.2E3)
print ("a:", a, "type:", type(a))
print ("b:", b, "type:", type(b))

a=complex(1+2j, 2-3j)
print (a, type(a))

a=complex(5.3)
print ("a:", a, "type:", type(a))

a= "5.5+2.3j"
b=complex(a)
print ("Complex number:", b)

a=5+6j
print ("Real part:", a.real, "Coefficient of Imaginary part:", a.imag)