list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list1.append('e') #list_name.append to add a character to a list
print ("List after appending: ", list1)

list1 = ["Rohan", "Physics", 21, 69.75]

list1.insert(2, 'Chemistry')
print ("List after appending: ", list1)

list1.insert(-1, 'Pass')
print ("List after appending: ", list1)

# Original list
list1 = [1, 2, 3]
# Another list to extend with
another_list = [4, 5, 6]

list1.extend(another_list)
print("Extended list:", list1)


