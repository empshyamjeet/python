text = "madam"
text1 = "madam2"
def is_palindrome(s):
    # Check if the string is equal to its reverse
    return s == s[::-1]
print(is_palindrome(text))  # Output: True
print(is_palindrome(text1))  # Output: False