# 1. Write a Python function called is palindrome that takes a string s as input and returns True if s is a palindrome (reads the same forwards and backwards), otherwise returns False.

def is_palindrome(s):

    s = ''.join(char.lower() for char in s if char.isalnum())

    return s == s[::-1]

# 2.Write a Python function called calculator that takes three arguments: num1 (float), num2 (float), and operation (string). The function should perform the specified operation ('add', 'subtract', 'multiply', 'divide') on numl and num2 and return the result
def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operation"

# 3. Write a python function called word Counter that takes a string "S" as an input, and return the count of each character in word or in "S". e.g pass S = "upflairs pvt ltd" u->1 p->2 l->2 and so on 

def word_counter(S):
    char_count = {}
    for char in S:
        if char.isalnum():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    return char_count

# 4. Write a Python function called right_triangle_pattern that takes an integer n as input and prints a right triangle pattern of n rows. Each row should contain i asterisks (*), where i is the row number. Example: For n = 5, the pattern should be:  
#*
# **
# ***
# ****
# *****

def right_triangle_pattern(n):
    for i in range(1, n + 1):
        print('*' * i)

# 5. Write a Python function called multiplication table that takes an integer n as input and prints the multiplication table of n up to 10.


def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

