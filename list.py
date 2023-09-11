import random
# s = [2, 4,8, 12, 14 ,18, 136, 94, 23]
# i= 0
# while i < len(s):
#     print(s[i])
#     i += 1

# s = [2, 4,8, 12, 14 ,18, 136, 94, 23]
# for x in s:
#     if x % 2 == 0:
#         print("this is even number: ", x)
#     else:
#         x % 2 != 0
#         print("this is odd number: ", x )

# list = ["a","b","c","d"]  
# x = len(list)
# for j in range(x):
#     print(list[j],"is available in positive index",j,"and negative index",j-x)

# l = [10,20,30,40,10,20,10,10]
# target = int(input("enter the value the search: "))
# if target in l:
#     print(target,"available and its first occurrence is at:",l.index(target))
# else:
#     print(target,"not available")    

# matrix form
# x = [[10,20,30],[40,20,50],[70,20,80]]
# for r in x:
#     print(r)
# for i in range(len(x)):
#     for j in range(len(x[i])):
#         print(x[i][j], end= "")
#     print()

# l1 = [2 ** x for x in range(1,11)]
# print(l1)

# l1 =[2**x for x in range(1,12)if x %2 ==0]
# print(l1) 

# method of list

# to add element to list upto 100which are divisible by 10

# l =[]
# for x in range(101):
#     if x % 10 == 0:
#         l.append(x)
# print(l)

# insert methot
# l = [10, 20 ,50,20 ,40 ,20]
# l.insert(5,66)
# l.insert(77, 9999)
# l.insert(-10,333)
# print(l)

# extend method
# l1 = [10,30,40,50]
# l2 = ["s", "m", "d"]
# l1.extend(l2)
# print(l1)

# remove method
# l = [10, 30 ,50 ,60 ,80, 40]
# l.remove(10)
# print(l)

# pop method
# l = [10 ,20 ,30 ,40 ,50 ,60]
# l.pop(3)
# print(l)
# l.pop()
# print(l)

# cleae method 
# l = [10,20 ,30 ,40, 50, 60]
# l.clear()
# print(l)

# copy method
# l = ["apple", "mango", "banana", "grapes"]
# l2 = l.copy()
# l2[2] = "papaya"
# print(id(l2))
# print(id(l))

# deep copy method
# l = ["apple", "malngo", "banana", "grapes"]
# l2 = copy.deepcopy(l)
# l2.append("papaya")
# print(id(l2))
# print(id(l))


# l = [30 ,60, 3, 18, 0 ,10]
# l.sort()
# print(l)

# l.sort(reverse = True)
# print(l)

# x = [[10,20,30],[40,50,60],[60,70,80]]
# for i in x:
#     # print(i)
#     for r in i:
#         print(r ,end =" ")
#     print()
# for i in range(len(x)):
#     # print(i)
#     for r in range(len(x[i])):
#         print(x[i][r] ,end =" ")
#     print()


# words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
# l = [x[0] for x in words]
# print(l)

# num1=[10,20,30,40] 
# num2=[30,40,50,60]
# num3=[ i for i in num1 if i not in num2] 
# print(num3) 


# words="the quick brown fox jumps over the lazy dog"
# print(words)  
# l=[[w.upper(),len(w)] for w in words.split()] 
# print(l)

# Write a program to display unique vowels present in the given word?
# vowel = ["a","e","i","o","u"]
# word =input("enter the word from the user: ")
# l = [[x for x in word if x in vowel]
# print(l)

# vowels=['a','e','i','o','u'] 
# word=input("Enter the word to search for vowels: ") 
# found=[] 
# for letter in word: 
#     if letter in vowels: 
#         if letter not in found: 
#             found.append(letter) 
# print(found) 
# print("The number of different vowels present in",word,"is",len(found))

# lib = [4,8,2,4,0,3]
# multiply = [2*x for x in lib ]
# print(multiply)

# lib = [4,8,2,4,0,3]
# power =[x**2 for x in lib]
# print(power)


# one = ['a', 'b', 'c', 'd', 'e']
# one.reverse()
# print(one)
# 2nd method
# print(one[::-1])


# names = ["bob" , "mike" ,"jhon"]
# list = ["hi, "+ x for x in names]
# print(list)

# names = ["Bob", "Mike", "John", "Jerry"]
# list = [x[0] for x in names]
# print(list)

# names = ["Bob", "Mike", "John", "Jerry"]
# len = [len(x) for x in names]
# print(len)


# one = ['a', 1, 'b', 'b', 4, '1']
# two = ['h', 'l', 1, 'a', 'j', '1']
# three = [x for x in one if x in two]
# print(three)

# a = [5,1,6] 
# b = [3,2,4]
# # print(a+b)
# list = [x for x in a+b]
# print(list)

# ne = ['Jack', 'Brit', 'Lucas', 'Ben']
# two = [10, 15, 4, 6]
# list = [[ne[x],two[x]] for x in range(len(ne))]
# print(list)

# nl = [[4, 8], [15, 2], [23, 42]]
# nestedSum = [x + y for x , y in nl ]
# print(nestedSum)

# nl = [[4, 8], [15, 2], [23, 42]]
# list = [x>y for x,y in nl]
# list = [x<y for x,y in nl]
# print(list)

# a = [5, 1, 6]
# b = [3, 2, 4]
# sum = []
# print(sum)dout

# names = ['Bob', 'Mike', 'John', 'Jerry']
# list = [x == "john" for x in names]
# print(list)

# lib = [4, 8, 2, 4]
# list = [x > 6 for x in lib]
# print(list)

# ternary operator
# one = [1, 2, 3, 4, 5, 6, 7]
# list = [x if x%2 ==0 else x*2 for x in one]
# print(list)

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list = [x for x in a if x % 2 == 0]
# print(list)

# all_clients = [{'name': 'Jack', 'age': 10, 
# 'balance': 100}, {'name': 'Brit', 'age': 15, 
# 'balance': 200}, {'name': 'Lucas', 'age': 4, 
# 'balance': 300}, {'name': 'Ben', 'age': 6, 
# 'balance': 400}]

# list = [x["name"] for x in all_clients if x["age"] >= 11 or x["balance"]>= 300]
# print(list)

# one = [1, 2, 3, 4, 5]
# two = ["a", "b", "c", "d", "e"]
# three = dict([(one[x],two[x]) for x in range(len(one))])
# print(three) 

# three = {one[x]:two[x] for x in range(len(one))}
# print(three)


# list = [8,7,24,36,28,25]
# l = [x for x in list if x%2==0]
# print(l)


# 1. Write a Python program to sum all the items in a list.
# list = [10,20,30,50,60,10]
# sum = 0 
# for x in list:
#     sum = sum + x
# print(sum)


# 2. Write a Python program to multiply all the items in a list.
# list = [10,30,5,4,8,9,16,20]
# multiply = 1
# for x in list:
#     multiply = multiply * x
# print(multiply)


#3. Write a Python program to get the largest number from a list.
# list = [30,36,5,20,10,36,16,23]
# print(max(list))


#4. Write a Python program to get the smallest number from a list.
# list = [30,36,5,20,10,36,16,23]
# print(min(list))


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# list.sort()
# print(list)dout


#7. Write a Python program to remove duplicates from a list.
# list = [10,30,20,40,40,10,20,30]
# l = []
# for x in list:
#     if x not in l:
#         l.append(x)
# print(l)


# 8. Write a Python program to check if a list is empty or not.
# l = []
# l =[10, 20]
# if not l:
#     print("list is empty")
# else:
#     print("not empty")

# 9. Write a Python program to clone or copy a list.
# list = [10,30,20,60,40,80]
# print(id(list))
# l1 = list.copy()
# print(l1)
# print(id(l1))

# 10. Write a Python program to find the list of words that are longer than n from a given list of words
# n = 3
# word = "the quick brown fox"
# list = [x for x in word.split(" ") if len(x)>n]
# print(list)

# # 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# list1 = [10,20 ,30,40,50,60]
# list2 = [5,6,20,16,18,80]
# for x in list1:
#     for y in list2:
#         if x == y:
#             print(True)dout


# 24. Write a Python program to append a list to the second list.
# list1 = [10,20,30]
# list = [10,40,50]
# list1.extend(list)
# print(list1)
# 2nd method
# l = list1 + list
# print(l)


# 19. Write a Python program to calculate the difference between the two lists.
# list = [10,20,30,40]
# set =set(list)
# print(set)
# l = list(set)
# print(l)

# 46. Write a Python program to select the odd items from a list.
# list = [7,9,18,23,22,35,36,16,20]
# l = []
# for x in list:
#     if x % 2 != 0:
#         l.append(x)
# print(l)


# 47. Write a Python program to insert an element before each element of a list.
# list = ["red","yellow","brown"]
# list1 = ["hi, "+ x for x in list]
# print(list1)

# 48. Write a Python program to print nested lists (each list on a new line) using the print() function.
# list = [[10,20],[30,40],[40,50],[60,70],[80,90]]
# for x in list:
#     print(x)


# 54. Write a Python program to concatenate elements of a list.
# list = ["red","brown","pink","blue"]
# print("".join(list))

# 56. Write a Python program to convert a string to a list.
# string = "what is your name"
# print(string.split(" "))

# 68. Write a Python program to extend a list without appending.
# l1= [10, 20, 30]
# l2= [40, 50, 60]
# l = l2+l1
# print(l)

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# List = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
# s = [0,4,5]douot


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
# list = [20,33,40,45,27,18,29,37]
# list1 = [x for x in list if x%2!=0]
# print(list1)

# 15.Write a Python program to shuffle and print a specified list.
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# random.shuffle(color)
# print(color)

# 16.Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

# list= []
# for x in range (1,31):
#     list.append(x*x)
# print(list[:5])  
# print(list[-5:]) 

# 20. Write a Python program to access the index of a list.
# list = [10,20,30,40,50,60]
# l = len(list)
# for x in range(l):
#     print(x ,list[x])


# 21. Write a Python program to convert a list of characters into a string.
# list = ["ab","cd","ef","gh","ij","kl"]
# l = "".join(list)
# print(l)


# 22. Write a Python program to find the index of an item in a specified list.
# list = [10,30,46,76,56,40]
# l= list.index(76)
# print(l)

# 25. Write a Python program to select an item randomly from a list.
# list = [29,60,590,40,70,20]
# l = random.choice(list)
# print(l)
 
# 27. Write a Python program to find the second largest number in a list.
# list = [10,50,2,56,68,52]
# l = sorted(list, reverse = True)
# print(l[1])


# 28. Write a Python program to find the second smallest number in a list.
# list = [10,30,59,690,70]
# l = sorted(list)
# print(l[1])


# 29. Write a Python program to get unique values from a list.

# list = [10,20,10,30,40,30,50,40,60,70,80,60]
# set = set(list)
# newlist = list(set
# print(newlist)

# 8. Python List exercise with solutions
# Excercise: 1 Write a python program to find the max item from a list without using the max
# function
# l1=[4,6,2,8,1]
# l1.sort(reverse=True)
# print(l1[0])

# Excercise 2 Find the reverse of a number provided by the user(any number of digit)
# n = int(input("enter the number from the user: "))

# Excercise 3 Take a number from the user and find the number of digits in it.
# n = int(input("enter the number from the user: "))
# digit = list(map(int,str(n)))
# print(digit)
# print(len(digit))

# Exercise 4: Write a python program to remove all the duplicates from a list
# l1=[1,2,3,3,3,4,4,5,6,7,8,9,9]
# y =set(l1)
# print(list(y))

# Exercise 5: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

# Exercise 6: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# l = [i+j for i,j in zip(list1,list2)]
# print(l)

# Exercise 7: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]
# l = [i**2 for i in numbers ]
# print(l)

# Exercise 8: Concatenate two lists in the following order
# Expected result:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# for i in list1:
#     for j in list2:
#         print(i+j)

# Exercise 10: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list = []
# for x in list1:
#     if x!="":
#         list.append(x)
# print(list)

# result = list(filter(lambda X : x != "",list1))


# Exercise 11: Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)

# Exercise 12: Extend nested list by adding the sublist
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)

# Exercise 13: Replace list’s item with new value if found
# list1 = [5, 10, 15, 20, 25, 50, 20]
# x = list1.index(20)
# list1[x]=200
# print(list1)

# Exercise 14: Remove all occurrences of a specific item from a list.
# list1 = [5, 20, 15, 20, 25, 50, 20]
# list2 = [x for x in list1 if x!=20]
# print(list2)

# Excercise 15 :Write a program that can perform union and intersection on 2 given list.
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
list1 = []
if l1 in l2:
    list1.append(l2)
print(list1)
