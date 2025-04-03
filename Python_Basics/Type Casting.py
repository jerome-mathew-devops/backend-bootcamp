a=True; #Boolean true=1 and false=0
b=10.5;
c=a+b;

print (c);

# Explicit
a="man"
b=18.4
c=17
d=True

a=int(b)
print ("A is now a", a, type(a))

b=bool(b)
print ("B is now a", b, type(b))

i=str(b)
print ("C is now a", i, type(i))

d=float(c)
print ("A is now a", c, type(c))

# Implicit (Automatic)

a, b=4, 16.7
c=a+b
print(c, type(c))