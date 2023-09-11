# fruits = ["apple", "banana", "grapes", "papaya", "pear", "mango"]
# for x in fruits:
#     print(x)

# for x in "banana":
#     print(x)

# exit the loop        

# for x in fruits:
#     print(x)
#     if x == "grapes":
#         break

# fruits = ["apple", "banana","grapes", "papaya", "pear", "mango"]
# for x in fruits:
#     if x == "papaya":
#         break
#     print(x)

# print("----------------")

# fruits = ["apple", "banana", "grapes", "papaya", "pear", "mango"] 
# for x in fruits:
#     if x == "grapes":
#         continue
#     print(x)

# using the range function

# for x in range (6):
#     print(x)

# using the start parameter

# for x in range (2,6):
#     print(x)


# else in for loop

# for x in range (6):
#     print(x)
# else:
#     print("finally finished")


# for x in range (6):
#     if x == 3: break
#     print(x) 
# else:
#     print("finally finished")


# nested loop 

# adj = ["red", "big", "tasty"] 

# fruits = ["apple", "banana", "cherry", "papaya"]
# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x in [0 , 1 , 2]:
#     pass

# cow = ["2", "6", "8", "4", "3", "9"]
# dog = ["4", "7", "8", "6", "5", "3"]
# sum = 0
# for x in cow:
#      for y in dog:
#          sum = sum + int(x) + int(y)
# print(sum)

# s =eval(input("enter the list from the user: "))
# sum = 0
# for x in s:
    # sum1 = sum + x
    # print("the sum: ", sum1)
    # print(x)


# s = input("enter the string: ")
# i = 0
# for x in s:
#     print("character: ", x ,"index: ", i)

#     i += 1


# s = input("enter the string from the user: ")
# i = 0
# for x in s:
#     print(i)
#     i += 1

# s = input("enter the value from the user: ")
# i = 0
# for x in s:
#     print("element : ",x ,"index value: ",i)
#     i += 1 

# s = input("enter the string from the user: ")
# print(len(s))
# for x in s: 
#     print(x)

# s = input("enter the number from the user: ")
# for x in s:
#     print(x)
# print(type(x))

# s = input("enter the string from the use:")
# # print(s[::-1])
# l = len(s)
# s1 = ""
# while 0 <= l-1:
# #    s1 += s[l-1] 
#    s1 = s1 + s[l-1]
#    l -= 1
# print(s1)   

# s = input("enter the string from the user: ")
# l = len(s)
# for x in range (l):
#     print(x)
#     if s[x] != s[l-x-1]:
    
    
# s = input("enter the string from the user: ")
# print(s[:])
# index = 0
# for x in s :
#     print(x, index)
#     index += 1

# s = input("enter the string from the user: ")
# l = len(s)
# for x in range (l):
#     print(s[x])

# s = input("enter the string from the user: ")
# l = len(s)
# for x in range(l):
#     # print(x)
#     print(s[l-x-1])

# s = input("enter the string from the user: ")
# l = len(s)
# s1 = ""
# while 0 <= l-1:
#     s1 +=s[l - 1]
#     l -= 1
# print(s1)

# a company decided to give bonus to employee according to following criteria

# s = eval(input("enter the salary from the user: "))
# s1 = int(input("enter the year from the user: "))
# if s1 > 10:
#     print(10)

#  Print sum of all even numbers from 10 to 20
# sum = 0
# for x in range(10,20,2):
#     sum = sum + x
# print(sum)

#  Calculate the square of each number of list
# numbers = [1, 2, 3, 4, 5]
# for x in numbers :
#     square = x*x
#     print(square)


# Calculate the average of list of numbers
# numbers = [10, 20, 30, 40, 50]
# sum = 0
# l = len(numbers)
# for x in numbers:
#     sum = sum + x
#     average = sum / l
# print(average)

# Print all even and odd numbers upto 1 to 20
# for x in range(1 , 20):
#     if x % 2 == 0:
#         print("even number: ", x)
#     else:
#         print("odd number: ", x)

#  Count the total number of ‘m’ in a given string.
# name = "mariya mennen"
# # print(name.count("m"))

# 2nd method
# count = 0
# for x in name:
#     if x != "m":
#         continue
#     else:
#         count = count + 1
# print("total number of m is: ", count) 

# reversed a list

# # list1 = [10, 20, 30, 40]
# list1.reverse()
# print(list1)


# s = input("enter some string: ")
# output = ""
# for x in s:
#     if x.isalpha() :
#         output = output + x
#         previous = x 
#     else : 
#         output = output + previous*(int(x) - 1)
# print(output)      

# a = 0
# if a == 1 :
#     x = "an"
# else:
#     print(x)

s = "a4b5c3"
output = output1 = myOutput = ""
for x in s :
    if x.isalpha():
        output = x
    if x.isnumeric():
        output1 = x
    # print(output1)
    if output1.isnumeric():
        # print(output)
        newoutput = chr(ord(output)+ int(output1) )
        output1 = ""
        myOutput =  myOutput + output + newoutput
print(myOutput)

        
        
