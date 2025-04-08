s1="WORD"
print ("original string:", s1)
l1=list(s1)

l1.insert(3,"L")

print (l1)

s1=''.join(l1)
print ("Modified string:", s1)

import array as ar

# initializing a string
s1="WORD"
print ("original string:", s1)

# converting it to an array
sar=ar.array('u', s1)

# inserting an element
sar.insert(3,"L")

# getting back the modified string
s1=sar.tounicode()
print ("Modified string:", s1)

import io

s1="WORD"
print ("original string:", s1)

sio=io.StringIO(s1)
sio.seek(3)
sio.write("LD")
s1=sio.getvalue()

print ("Modified string:", s1)