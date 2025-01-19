# ==================== FUNCTIONS ====================

raahim_expense_list = [1200,1500,1600]
huzaifa_expense_list = [1200,1400,1700]

# Raahim's Expense
total = 0
for expense in raahim_expense_list:
    total = total + expense # total += expense
print("Raahim's total Expense: ", total)

# Huzaifa's Expense
total = 0
for expense in huzaifa_expense_list:
    total = total + expense
print("Huzaifa's total Expense: ", total)

"""
Since we are repeating the same code more than once, we can encapsulate it within a function.
"""

# Calculating the total expense by function
def calculate_total_expense(expense_list): 
    """
    Syntax of function: def function_name(function_arguments):
                            code here
    """
    # Don't worry guys it is the same code :)
    total = 0
    for expense in expense_list:
        total = total + expense
    return total

raahim_total = calculate_total_expense(raahim_expense_list)
huzaifa_total = calculate_total_expense(huzaifa_expense_list)

print("Raahim's total Expense: ", raahim_total)
print("Huzaifa's total Expense: ", huzaifa_total)

# Simple add function
def addition(a, b):
    sum = a+b;
    return sum;

n = addition(5,6)
print("Sum: ", n)


# Named arguments
def addition(a, b):

    print("a: ", a)
    print("b: ", b)

    sum = a+b;
    print("Sum inside function: ", sum)

    return sum;

n = addition(b=5, a=6)
print("Sum outside function: ", n)

# Document strings aka Doc Strings
def addition(a, b):
    """
    A simple add function which takes two integer arguments and returns the sum of them.
    """
    sum = a+b;
    return sum;

n = addition(5, 6)
print("Sum: ", n)