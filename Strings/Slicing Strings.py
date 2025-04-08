var = "HELLO PYTHON "
print(var[0]) 
print(var[7])  
print(var[11])  
print(var[12]) 

var = "HELLO PYTHON"
print(var[-1]) 
print(var[-5])  
print(var[-12])  

var="HELLO PYTHON"
var[7]="y"  #Error because the string is immutable
print (var)

var="HELLO PYTHON"

print ("var:",var)
print ("var[3:8]:", var[3:8])

var="HELLO PYTHON"
print ("var:",var)
print ("var[3:8]:", var[3:8])
print ("var[-9:-4]:", var[-9:-4])

var="HELLO PYTHON"
print ("var:",var)
print ("var[0:5]:", var[0:5])
print ("var[:5]:", var[:5])

var="HELLO PYTHON"
print ("var:",var)
print ("var[6:12]:", var[6:12])
print ("var[6:]:", var[6:])

var="HELLO PYTHON"
print ("var:",var)
print ("var[0:12]:", var[0:12])
print ("var[:]:", var[:])