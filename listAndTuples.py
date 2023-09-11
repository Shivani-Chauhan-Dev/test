# thelist = ["apple" ,"banana" ,22 ,"tomato" ,66.6 ,"mohit", "sagar"]
# print(thelist)

# print(len(thelist))

# print(thelist[2])

# print(thelist[0])

# print(thelist[5])

# thelist.insert(2,"shivani")
# print(thelist)

# thelist.remove(22)
# print(thelist)

# thelist.count(22)
# print(thelist)



# i = 0
# while  i < (len(thelist)) :
#     print(thelist[i])
#     i += 1

# i = 0
# while  i < (len(thelist)) :
#     i += 1
#     if  i == 5:
#         thelist.insert(6,"shivani")
#         print(thelist)

#  tuple
# t = (10,20,30,40,10,10)
# print(t)
# print(type(t))

# t =()
# print(type(t))

# t = (10,)
# print(t)
# print(type(t))

# by using tuple function

# list = [10,20,30,40]
# print(list)
# print(type(list))
# print(tuple(list))
# print(type(tuple(list)))

# t = tuple(range(2,20,4))
# print(t)

# accessing element of tuple
# t = (10,20,30,40,50,60)
# print(t[3])
# print(t[-1])

# print(t[0:4])
# print(t[:: 2])

# importan function of tuple
# t = (70,10,20,30,40,50,60,20,20)
# print(len(t))
# l=t.count(20)
# print(l)

# print(t.index(10))
# print(t.index(20))

# print(sorted(t))
# print(sorted(t,reverse=True))

# cmp()

# t1 = (10, 20, 30, 40)
# t2 = (30, 40, 50, 60)
# t3 = (10, 40, 50, 60)
# print(cmp(t1,t2))
# print(cmp(t1,t3))
# print(cmp(t2,t3))
# print(cmp(t3,t1))dout

# tuple packing and unpacking

# a =10
# b=20
# c=30
# d=40
# t= a,b,c,d
# print(t)

# t= (19,39,48,59)
# a,b,c,d = t
# print(a,b,c,d)

# tuple comprehension
# t =(2**x for x in range(1,20))
# print(type(t))

# Write a program to take a tuple of numbers from the keyboard and print its sum and 
# average?

# tuple =eval(input("enter tuple of number: "))
# sum = 0
# t = len(tuple)
# for x in tuple:
#     sum = sum + x
#     average = sum/t
# print(sum)
# print(average)



# 1. Write a Python program to create a tuple.
# t = ()
# print(type(t))

# 2. Write a Python program to create a tuple with different data types.
# t = (10,"sh",6.86,[10,20])
# print(t)

# 3. Write a Python program to create a tuple of numbers and print one item.
# tuple = (10,30,40,20,10,16)
# print(tuple)
# tuple = 10,
# print(tuple)

# 4. Write a Python program to unpack a tuple into several variables.
# tuple = (10,20,30,40)
# a,b,c,d = tuple
# print("a=",a,"b=",b,"c=",c,"d=",d)

# 5. Write a Python program to add an item to a tuple.
# t1 = (10,20,40,50)
# t2= 10,
# print(t1+t2)

# list = [10,40,50,60]
# list.append(10)
# print(list)
# print(tuple(list))

# 6. Write a Python program to convert a tuple to a string.
# tuple=("sh","ab","mo")
# t = "".join(tuple)
# print(t)

# 7. Write a Python program to get the 4th element from the last element of a tuple.
# t = (10,20,30,40,50,10,40,60,70,80)
# print(t[-4])


# 8. Write a Python program to create the colon of a tuple.
# t = (10,30,40,50,60,80)dout

# 9. Write a Python program to find repeated items in a tuple.
# tuple = (10,30,26,16,18,66,10,10,10)
# t=tuple.count(10)
# print(t)


# 10. Write a Python program to check whether an element exists within a tuple.
# tuple = eval(input("enter the element : "))
# t1 = (10,20,40,50,50,60,80,16,20)
# if tuple in t1:
#     print("element is exixt")


# 11. Write a Python program to convert a list to a tuple.
# list = [10,30,16,18,20,24]
# t = tuple(list)
# print(t)

# 12. Write a Python program to remove an item from a tuple.
# tuple = (10,40,49,79,67,58,80)
# t = list(tuple)
# t.remove(10)
# tuple = tuple(t)
# print(tuple)dout

# 12. Write a Python program to remove an item from a tuple.
# tuple = (10,30,40,70,56,78,49,39)
# print(tuple[2::2])


# 14. Write a Python program to find the index of an item in a tuple.
# tuple = (10,40,60,70,40,80,99,20)
# print(tuple.index(60))


# 15. Write a Python program to find the length of a tuple.
# tuple = (10,60,50,40,44,56,66,16)
# t = len(tuple)
# print(t)

# 16. Write a Python program to convert a tuple to a dictionary.

# tuple = ((10,20),(40,50),(60,70),)
# t = dict(tuple)
# print(t)


# 17. Write a Python program to unzip a list of tuples into individual lists.
# list1 = [(10,20,30),(20,40,50),(60,70,80)]
# t= list(zip(*list1))
# print(t)

# 18. Write a Python program to reverse a tuple.
# t = (10,50,60,30,16,26)
# t1=reversed(t)
# print(tuple(t1))


# 19. Write a Python program to convert a list of tuples into a dictionary.
# list = [(2,3),(4,5),(6,7)]
# t = dict(list)
# print(t)

# 26. Write a Python program to calculate the product, multiplying all the numbers in a given tuple.
# tuple = (1,5,6,4,3,8)
# multiply = 1
# for x in tuple:
#     multiply = x*multiply
# print(multiply)


# 27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
# Original Tuple:

# tuple = ((10,6,4),(40,10,40),(30,50,2),(30,6,16))
# t = list(tuple)
# l1 =[]
# sum = 0
# for x in t:dout

# 28. Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values:

# tuple = ("40","52")
# t = (int(tuple[0]),int(tuple[1]))
# print(t)


# 29. Write a Python program to convert a given tuple of positive integers into an integer.
# tuple = (10,30,40)
# t = "".join(tuple)
# print(t)

# 11. Python Tuple Exercise with Solutions
# Exercise 1: Reverse the tuple
# tuple1 = (10, 20, 30, 40, 50)
# tuple1[::-1]
# print(tuple1)


# Exercise 2: Access value 20 from the tuple
# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])

# Exercise 3: Create a tuple with single item 50
# tuple = (50,)

# Exercise 4: Unpack the tuple into 4 variables
# tuple1 = (10, 20, 30, 40)
# a,b,c,d = tuple1
# print(a)
# print(b)
# print(c)
# print(d)

# Exercise 5: Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1,tuple2 = tuple2,tuple1
print(tuple1)
print(tuple2)