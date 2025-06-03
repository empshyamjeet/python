a=10
b=20
# Method 1: Using Arithmetic Operations
a = a + b
b = a - b
a = a - b
print("After swapping using arithmetic operations: a =", a, ", b =", b)
# Method 2: Using Bitwise XOR
a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping using bitwise XOR: a =", a, ", b =", b)
# Method 3: Using Tuple Unpacking
a = 10
b = 20
a, b = b, a
print("After swapping using tuple unpacking: a =", a, ", b =", b)
# Method 4: Using a Temporary Variable
a = 10
b = 20
temp = a
a = b
b = temp
print("After swapping using a temporary variable: a =", a, ", b =", b)
# Method 5: Using Python's built-in function
a = 10
b = 20
a, b = b, a
print("After swapping using Python's built-in function: a =", a, ", b =", b)
# Method 6: Using List
a = 10
b = 20
lst = [a, b]
lst[0], lst[1] = lst[1], lst[0]
a, b = lst
print("After swapping using list: a =", a, ", b =", b)
