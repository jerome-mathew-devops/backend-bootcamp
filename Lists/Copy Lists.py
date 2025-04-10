import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a shallow copy
shallow_copied_list = copy.copy(original_list)
# Modifying an element in the shallow copied list
shallow_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Shallow Copied List:", shallow_copied_list)

import copy
# Original list
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Creating a deep copy
deep_copied_list = copy.deepcopy(original_list)
# Modifying an element in the deep copied list
deep_copied_list[0][0] = 100
# Printing both lists
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using slice notation
copied_list = original_list[1:4]
# Modifying the copied list
copied_list[0] = 100
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)

# Original list
original_list = [1, 2, 3, 4, 5]
# Copying the list using the list() constructor
copied_list = list(original_list)
# Printing both lists
print("Original List:", original_list)
print("Copied List:", copied_list)



