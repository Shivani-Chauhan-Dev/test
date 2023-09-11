import re
# city = input("enter the city name from the user: ")
# list = ["Hadrabad" , "Delhi" , "Meerut" , "GOa"]
# list2 = [x.lower() for x in list]
# if city.lower().strip() in list2:
#     print("your city is available" , city)
# else:
#     print(city, "Not available... please enter the valied city name")
# flag = False
# l = len(list)
# for x in range(l):
#     # print(list[x])
#     if list[x].lower().strip() == city.lower().strip():
#         flag = True
# if flag == True:
#     print("city is available", city)
# else:
#     print("city is not available", city)


# s = "python is very easy"
# s2=s.upper()
# print(s2)

# s = "PYTHON IS NOT EASY TO UNDERSTAND"
# print(s.lower()
# m = "SomE woDS aRe VEry DIFFecult"
# print(m.swapcase())

# s = "the python classes by durga sir"
# print(s.title())

# s = "the"
# print(s.capitalize())

# # s = "learning python is very easy"
# print(s.startswith("Easy"))
# print(s.endswith("easy"))
# print(s.startswith("learning"))

# to print characters at odd position and even position for the given 
# s = input("enter the given string from the user: ")
# print("character of even position: ", s[ :: 2])
# print("character of odd position: " , s[1 :: 2])

# without slice operator

# s = input("enter the string from the user: ")
# i = 0 
# print("the character at even position: ")
# while i < len(s):
#     print(s[i] , end = ",")
#     i = i + 2
# print()
# i = 1
# print("the character of odd position: ")
# while i < len(s):
#     print(s[i], end = ",")
#     i = i + 2

# input = "B4A1D3"
# output = "ABD134"
# s= input("enter some string from the user: ")
# s1 = s2 = output= ""
# for x in s:
#     if x.isalpha():
#         s1 = s1 + x
#     else:
#         s2 = s2 + x
# for x in sorted(s1):
#     output = output + x
# for x in sorted(s2):
#     output = output + x
# print(output)   

# s1 = input("enter first string: ")
# s2 = input("enter second string :")
# output = ""
# i = j = 0
# while i < len(s1) or j < len(s2):
#     output = output + s1[i] + s2[j]
#     i += 1
#     j += 1
# print(output)

# s1 = input("enter first string: ")
# s2 = input("enter second string: ")
# output = ""
# i = j = 0
# while i < len(s1) or j < len(s2):
#     if i < len(s1):
#         output = output + s1[i]
#         i += 1
#     if j < len(s2):
#         output = output + s2[j]
#         j += 1
# print(output)


# s = input("enter the 4 digit strin from the user: ")
# l = len(s)
# for x in range(l):
#     print(s[l-x-1] , end = ",")

# Python program to print even length words in a string
# s = input("enter the some string from thwe user: ")
# s2 = s.split(" ")
# for x in s2:
#     if len(x) % 2 == 0:
#         print(x)

#  Print characters from a string that are present at an even index number
# m = input("enter the string from the user:")
# l = len(m)
# for x in range (l):
#     if x % 2 == 0:
#         print(m[x])

#  Remove first n characters from a string

# # m = input("enter the string from the user: ")
# print(m[2:])
# print(m[::2])

# Check if the first and last number of a list is the same
# m = [10, 20 ,30 , 10]
# if m[0] == m[-1]:
#    return True

# Display numbers divisible by 5 from a list
# # m = [10,20,18,26,30,40]
# for x in m:
#     if x % 5 == 0:
#         print(x)

# Return the count of a given substring from a string
# str = "Emma is good developer. Emma is a writer"
# print(str.count("Emma"))

# 6. Python string Excercise with solutions

# Exercise 1: Return the count of a given substring from a string
# Write a program to find how many times substring “radha” appears in the given string

# sentence="radha is most beutiful,radha is queen of vraj,radha is most beloved to govind"
# y = sentence.count("radha")
# print(y)

# Exercise 2: Print characters from a string that are present at an even index number

# n = input("enter the string from the user: ")
# print(n[1::2])

# Exercise 3: Write a program to remove characters from a string starting from zero up to n and return
# a new string.
# n = input("enter the string from the user: ")
# print(n[2::])
# print(n[::2])

# Exercise 4 1A: Create a string made of the first, middle and last character
# n = input("enter the string from the user: ")



# Excercise 5 :Count the frequency of a particular character in a provided string. Eg 'hello how are you'
# is the string, the frequency of h in this string is 2.
# x='hello how are you'
# y = x.count("h")
# print(y)

# Excercise 6:Find the index position of a particular character in another string.
# a = input("enter the text")
# b = input("enter the character: ")
# print(a.index(b))

# Excercise 7: Write a program which can remove a particular character from a string.
# n ="shivani"
# print(n.replace("i",""))


# Exercise 8: Append new string in the middle of a given string
# a ="absdefg"
# b = "chauhan"
# l = len(a)
# mid = l//2
# s = a[mid:]
# s2 = a[:mid]
# y =s2+b+s
# print(y)

# Exercise 9: Create a new string made of the first, middle, and last characters of each input string
# s1 = "japan"
# s2 = "india"
# l=len(s1)//2
# l2=len(s2)//2
# y = s1[0]+s2[0]+s1[l]+s2[l2]+s1[-1]+s2[-1]
# print(y)

# Exercise 10: Arrange string characters such that lowercase letters should come first

# new post
# Creating a string using single quotes:
# str = 'hello world'
# print(str)

# Creating a string using double quotes
# str2 = "hello world "
# print(str2)

# Length of a String
# str = "hello world how are you"
# print(len(str))

# Using a “for loop” to traverse a string
# str1 = "data science"
# for i in str1:
#     print(i)

# Using range() to traverse a string:
# str1 = "how are you"
# l = len(str1)
# for i in range(l):
#     print(i)

# String Slicing
# string = "hello,world!"
# print(string[0:5])
# print(string[7:])
# print(string[-6:-1])
# print(string[::2])
# print(string[::-1])

# String Concatenation:
# str1 = "hello"
# str2 = " world"
# l = str1 + str2
# print(l)

# join method
# string = ["hello","world"]
# result = " ".join(string)
# print(result)

# string = "hello , world!"
# new_string = "j" + string
# new_string2 ="j"+ string[1:]
# print(new_string)
# print(new_string2)

# Counting Characters in a String
# string ="hello, world!"
# count = 0
# for i in string:
#     if i == "l":
#         count+=1
# print(count)

# The 'in' Operator in Python Strings:
# string = "hello,woeld!"
# if "l" in string:
#     print("l present in the given string")
# else:
#     print("not present")

# String Comparison in Python:
# String Comparison Operators in Python:
# str1 = "hello"
# str2 = "hello ,world!"
# if str1 == str2:
#     print("The string are equals")
# else:
#     print("The strings are not equals")


# string1 = "Hello"
# string2 = "hello"
# if string1.lower() == string2.lower():
#     print("The string are equals")
# else:
#     print("The string are not equals")

# capitalize()
# str = "hello ,world!"
# print(str.capitalize())

# casefold()
# str = "Hello,World"
# casefolded = str.casefold()
# print(casefolded)

# center()
# str = "hello ,world!"
# centered = str.center(10,"-")
# print(centered)

# count()
# str = "hello,world!"
# count = str.count("l")
# print(count)

# encode()
# str = "hello, world!"
# encod = str.encode()
# print(encod)

# endswith()
# str = "hello , world!"
# endswith = str.endswith("world")
# print(endswith)

# expandtabs()
# str = "hello\t world"
# expended = str.expandtabs(4)
# print(expended)

# find()
# str = "hello, world"
# print(str.find("l"))

# format()
# name = "Alice"
# age = 24
# string = "my name is{0} and i am {1} years old."
# formatted = string.format(name,age)
# print(formatted)

# index()
# str = "hello ,world!"
# print(str.index("world"))

# isalnum()
# str = "helloworld123"
# print(str.isalnum())

# isalpha()
# str = "hello"
# print(str.isalpha())

# isdigit()
# string = "123456"
# print(string.isdigit())

# Parsing Strings in Python:
# Splitting Strings: 
# str = "hello, world,!"
# print(str.split(","))

# Extracting Substrings:
# str = "hello,my name is john doe. i am 26 year old."
# pattern = r"(\b\w+\b)"
# matches = re.findall(pattern,str)
# print(matches)

# Format Operator in Python Strings:
# name ="Alice"
# age = 24
# str = "my name is %s and i am %d year old."%(name,age)
# print(str)

# name = "Alice"
# age = 24
# height = 1.65 
# str = "my name is %s and i am %d years old, and my height is %f meters."%(name,age,height)
# print(str)

# Mathematical Operations on Strings in Python:
# str1 = "hello"
# str2 = "hello"
# print(str1+str2)
# print(str1*4)

# Using eval():

# expression = "2+3*4"
# print(eval(expression))

# Exercise 19: Split a string on hyphens

# str1 = "Emma-is-a-data-scientist"
# y = str1.split("-")
# for i in y:
#     print(i)


# Exercise 14: Find all occurrences of a substring in a given string by ignoring the case
# str1 = "Welcome to USA. usa awesome, isn't it?"
# str2 = str1.upper()
# print(str2.count("USA"))


# Excercise 27: write progrme to count the number of vowels in the string
# string = "Milind Dattatray Mali"
# vowel = ("AEIOUaeiou")
# count = 0
# for i in string:
#     if i in vowel:
#         count +=1
# print(count)

# Exercies 26: extract all the emailid for the given string
# string="Hi my name is Govind Das and my mail id is milindmali108@gmail.com and my org mai"
# y = string.split(" ")
# print(y)
# for i in y:
#     if ".com" in i:
#         print(i)

# Exercise 22: Removal all characters from a string except integers
# str1 = 'I am 25 years and 10 months old'
# y = str1.split(" ")
# l = []
# for i in y:
#     if i.isdigit():
#         l.append(i)
# print(l)
# print("".join(l))


# Exercise 23: Find words with both alphabets and numbers
# str1 = "Emma253 is Data scientist50000 and AI Expert"
# new = []
# y = str1.split(" ")
# for i in y:
#     if i.isalnum():
#         new.append(i)
# print(i)

# Exercise 20: Remove empty strings from a list of strings
# strlist = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# for i in strlist:
#     if i == "":
#         strlist.remove(i)
# print(strlist)


# Exercise 17: Reverse a given string
# str1 = "PYnative"
# print(str1[::-1])

# Exercise 16: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
sum = 0
average = 0
for i in str1:
    if i.isdigit():
        sum = sum + int(i)
print(sum)