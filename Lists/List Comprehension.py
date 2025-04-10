string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)  

original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)  

list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2] 
print (CombLst)

list1=[x for x in range(1,21) if x%2==0]
print (list1)

chars=[] #Using for Loop
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)

chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou'] #Using List Comprehension
print (chars)

squares = [x*x for x in range(1,11)]
print (squares)