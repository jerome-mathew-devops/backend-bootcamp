# Two lists to be joined
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
# Joining the lists
joined_list = L1 + L2

# Printing the joined list
print("Joined List:", joined_list)

# Two lists to be joined
L1 = [36, 24, 3]
L2 = [84, 5, 81]
# Joining the lists using list comprehension
joined_list = [item for sublist in [L1, L2] for item in sublist]
# Printing the joined list
print("Joined List:", joined_list)

# List to which elements will be appended
list1 = ['Fruit', 'Number', 'Animal']
# List from which elements will be appended
list2 = ['Apple', 5, 'Dog']
# Joining the lists using the append() function
for element in list2:
    list1.append(element)
# Printing the joined list
print("Joined List:", list1)

# List to be extended
list1 = [10, 15, 20]
# List to be added
list2 = [25, 30, 35]
# Joining the lists using the extend() function
list1.extend(list2)
# Printing the extended list
print("Extended List:", list1)
