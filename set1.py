#1. Write a Python program that prints "Hello, World!" to the console.
# print("Hello, World!")

#2. Create variables of each data type (integer, float, string, boolean, list, tuple, dictionary, set) and print their types and values.
integer_var = 10
# print(f"Type of {integer_var}: {type(integer_var)}, value: {integer_var}")


float_var = 3.14
# print(f"Type of {float_var}: {type(float_var)}, value: {float_var}")


string_var = "Hello"
# print(f"Type of {string_var}: {type(string_var)}, value: {string_var}")


boolean_var = True
# print(f"Type of {boolean_var}: {type(boolean_var)}, value: {boolean_var}")


list_var = [1, 2, 3]
# print(f"Type of {list_var}: {type(list_var)}, value: {list_var}")


tuple_var = (4, 5, 6)
# print(f"Type of {tuple_var}: {type(tuple_var)}, value: {tuple_var}")


dictionary_var = {"name": "John", "age": 25}
set_var = {7, 8, 9}
# print(f"Type of {dictionary_var}: {type(dictionary_var)}, value: {dictionary_var}")

#3. Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
number = list(range(1, 11))
# print(number)

# add
number.append(11)
# print(number)

# remove
number.remove(9)
# print(number)

# add
number.append(9)
# print(number)

# sort
number.sort()
# print(number)

#4. Write a Python program that calculates and prints the sum and average of a list of numbers.
num = [10, 20, 30, 40]
sum = 0
for i in num:
    sum = sum+i
# print(f"Sum {sum}, Average {sum/len(num)}")

#5. Write a Python function that takes a string and returns the string in reverse order.


def reverse_string(input_str):
    return input_str[::-1]


input_str = "Python"
reversed_str = reverse_string(input_str)
# print(reversed_str)

#6. Write a Python program that counts the number of vowels in a given string.
vowels = "aeiouAEIOU"
count = 0
input_string = "Helloo"
for char in input_string:
    if char in vowels:
        count += 1
# print(f"Number of vowels: {count}")

#7. Write a Python function that checks whether a given number is a prime number.
# primecheck = 3
# c=0
# for n in primecheck(range(2,)):
#     if primecheck%n==0:
#         c+=1
#     if c==2:
#         print(f"{primecheck} is a Prime Number")
#     else:
#          print(f"{primecheck} is not Prime Number")


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


number = 3
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#8. Write a Python function that calculates the factorial of a number.
def factorial(numb):
    if numb == 0:
        return 1
    else:
        return numb * factorial(numb-1)

# print(factorial(5))

#9. Write a Python function that generates the first n numbers in the Fibonacci sequence.


def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]


num = 5
fib = fibonacci(num)
#print(fib)


#10. List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.

square =[i**2 for i in range(1, 11)] 
#print(square)


