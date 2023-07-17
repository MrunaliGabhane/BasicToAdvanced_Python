def is_palindrome_number(number):
    num_str = str(number)

    return num_str ==  num_str[::-1]


print(is_palindrome_number(121))  # True
print(is_palindrome_number(123))  # False