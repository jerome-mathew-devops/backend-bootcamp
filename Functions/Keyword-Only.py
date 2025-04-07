def intr(amt,*, rate):  #The * forces the function to have only 1 Position arg and 1 key work which is the rate keyword
   val = amt*rate/100
   return val
   
interest = intr(1000, 10)
print(interest)