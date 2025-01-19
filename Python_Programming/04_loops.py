# ==================== LOOPS ====================

# Simple old method
expenses = [2100,2300,2500,2600,3000]
total = expenses[0] + expenses[1] + expenses[2] + expenses[3] + expenses[4]
print(total)

# Using loops
total = 0
for expense in expenses: # expense: 2100
    total += expense # total = total + expense = value + 2500 = value
print(total)

# Range Function
for number in range(10):
    print(number)
# Same output as above
for number in range(1,11):
    print(number)

# three arguments wala range
# for number in range(1,10):
#     print(number)

# In the expense example print month number and expense and in the end print total expense.
expenses = [2100,2300,2500,2600,3000]
total = 0
for i in range(len(expenses)):
    print(f"Month: {i+1}, Expenses: {expenses[i]}")
    total += expenses[i]
# Outside the body of loop
print(f"Total: {total}")

# Fruits Example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)
  if fruit == "banana":
    break

# Continue keyword is also called skipping keyword in python
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i*i)

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj: # x = big
  for y in fruits: # y = apple
    print(x, y)

    # red, apple
    # red, banana
    # red, cherry
    # big, apple
    # big, banana
    # big, cherry
    # tasty, apple
    # tasty, banana
    # tasty, cherry


    


