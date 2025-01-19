# ===================== LISTS =====================

# Variables
item1 = "milk"
item2 = "bread"
item3 = "eggs"
item4 = "veggies"

# Formation of List
items = ["milk", "bread", "eggs", "veggies"]
# Syntax: variable_name = [item1, item2, item3, item4]
"""
In lists all values have similar meaning
"""

# Printing list members
# print(items[0]) # First item  
# print(items[1]) # Second item 
# print(items[2]) # Third item
# print(items[-3]) # Fourth item

# Changing a list member
# items[0] = "pasta"
# print(items)

# List slicing
# print(items[0:2]) # slicing syntax = list_name[starting_index:ending_index] 
# # ending index is excluded from slicing.
# print(items[1:2])
# print(items[2:2])
# print(items[-1])

# # List functions
# items.append("burger")
# items.insert(2, "butter")
# print(items)


# List concatenation
food = ["pizza", "pasta", "samosa", "qorma"]
bathroom = ["facewash", "soap", "shampoo", "facecream"]
items = food + bathroom
print(items)

# Length functions
print(len(items))

# ===================== TUPLES =====================

coordinate = (10,15) #(x, y)
print(coordinate[0])
print(coordinate[1])
"""
In tuples all values have different meaning
"""
address = ("1st Street Robinsville", "London", "100001")
print(address)
print(address[1])