a=int(True)
print ("bool to int:", a)
a=float(False)
print ("bool to float:", a)
a=complex(True)
print ("bool to complex:", a)

# Check true
a = True
print(bool(a))
# Check false
a = False
print(bool(a))
# Check 0
a = 0.0
print(bool(a))
# Check 1
a = 1.0
print(bool(a))
# Check Equality
a = 5
b = 10
print(bool( a==b))
# Check None
a = None
print(bool(a))
# Check an empty sequence
a = ()
print(bool(a))
# Check an emtpty mapping
a = {}
print(bool(a))
# Check a non empty string
a = 'Tutorialspoint'
print(bool(a))