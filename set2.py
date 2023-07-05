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
