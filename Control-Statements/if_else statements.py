age=25
print ("age: ", age)
if age >=18:
   print ("eligible to vote")
else:
   print ("not eligible to vote")

amount = int(input("Enter your amount spent"))
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
else:
   if amount > 5000:
      discount = amount * 10 / 100
   else:
      if amount > 1000:
         discount = amount * 5 / 100
      else:
         discount = 0

print('Payable amount = ',amount - discount)

amount = int(input("Enter amount spent: "))
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)