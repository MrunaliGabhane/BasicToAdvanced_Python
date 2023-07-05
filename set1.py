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


#SET 2:-
#1. Print the following pattern
size = 5
for i in range(size):
    for j in range(i + 1):
        print(j+1, end=" ")
    #for move to next line
    print()


#2.  ### **Display numbers from a list using loop**

#Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

#- The number must be divisible by five
#- If the number is greater than 150, then skip it and move to the next number
#- If the number is greater than 500, then stop the loop   
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
        if num%5==0:
            if num > 500:
                break
            if num > 150:
                continue
            print(num)

#3. ### **Append new string in the middle of a given string**
#Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
str1 = "Ault"
str2 = "Kelly"
middle = len(str1) // 2 
s3 = str1[:middle] + str2 + str1[middle:] 
print(s3)


#4. ### **Arrange string characters such that lowercase letters should come first**
#Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
input_str = "PyNaTive"
lowercase = filter(str.islower, input_str)
uppercase = filter(str.isupper, input_str)
low= "".join(lowercase)
upp= "".join(uppercase)
#print(upp+low)


#5.### **Concatenate two lists index-wise**
#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
new_list = [x + y for x, y in zip(list1, list2)]
#print(new_list)

#6.  Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
new_list = [x + y for x in list1 for y in list2]
#print(new_list)


#7. ### **Iterate both lists simultaneously**
#Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, reversed(list2)):
   print(x, y)

#8. **Initialize dictionary with default values**
#In Python, we can initialize the keys with the same values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = {emp:defaults for emp in employees}
print(result)

#9.**Create a dictionary by extracting the keys from a given dictionary**
#Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
result = {key: sample_dict[key] for key in keys}
print(result)


#10.**Modify the tuple**
#Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1) 
list1[1][0]=222
print(tuple(list1))
