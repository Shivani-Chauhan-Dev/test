# # funtion -
# # def myfunction():
# #     print("hello my function")

# # myfunction()

# def my_function():
#     print("hello world")

# my_function()

# def sum(a,b):
#     print(a + b)

# sum(6,6)
# sum(5,4)
# sum(3,4)
# sum(9,8)
# sum(4,6)
# sum(3,9)
# sum(4,8)
# sum("hello ","world")

# def multiplication(a,b,c = 1):
#     # print(a * b * c)
#     return a * b * c

# print(multiplication(5,6,0) + 2) 
# print(multiplication(3,0,1) + 2)
# print(multiplication(2,6,9) + 2)
# print(multiplication(4,6,8) + 2)
# print(multiplication(7,8,4) + 2)
# print(multiplication(3,9) + 2)

# def findEvenOdd(a):
#     if a % 2 == 0 :
#         return True
#     else :
#         return False

# print(findEvenOdd(2))
# print(findEvenOdd(3))
# print(findEvenOdd(4))
# print(findEvenOdd(99))
# print(findEvenOdd(136))
# print(findEvenOdd(24))
# print(findEvenOdd(330))
# print(findEvenOdd(26))
# print(findEvenOdd(340))
# print(findEvenOdd(3000))
# print(findEvenOdd(38))
# print(findEvenOdd(32))

# def wholeNumber(a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False

# print(wholeNumber(0))
# print(wholeNumber(7))
# print(wholeNumber(3.44))
# print(wholeNumber(76))
# print(wholeNumber(6.66))

# def evenNumber(a,b):
#     if a + b % 2 == 0:
#         return True
#     else:
#         return False   

# print(evenNumber(3,6))
# print(evenNumber(2,1))
# print(evenNumber(4,9))
# print(evenNumber(2,4))
# print(evenNumber(5,8))
# print(evenNumber(4,4))
# print(evenNumber(2,2))
# print(evenNumber(6,6))

# def Even_number(v):
#     a = 1
#     while a <= v :
#         if a % 2 == 0:
#             print(a)
        
#         a += 1
       
# Even_number(6)
# print("---------------")
# Even_number(9)
# print("---------------")
# Even_number(3)
# print("---------------")
# Even_number(6)
# print("---------------")
# Even_number(8)
# print("---------------")
# Even_number(7)
# print("---------------")


# def oddNumber(v):
#     a = 0
#     while a <= v:
#         if a % 2 != 0:
#             print(a)
#         a += 1

# print(oddNumber(4)) 
# print("-----------")
# print(oddNumber(7))
# print("------------")
# print(oddNumber(19))
# print("------------")
# print(oddNumber(9))      

 
# def naturalNumber(a,b):
#     if a + b >= 0:
#         # print("natural")
#         return True
#     else:
#         return False
#         # print("int")    

# print(naturalNumber(2,6))
# print(naturalNumber(3,-6))
# print(naturalNumber(8,6))
# print(naturalNumber(0,0))
# print(naturalNumber(-4,8))
# print(naturalNumber(-6,-6))


# def add_subtract(a,b):
#     if a + b >= a - b:
#         return True
#     else:
#         return False 
# print(add_subtract(6,-4))
# print(add_subtract(6,0))
# print(add_subtract(-8,3))
# print(add_subtract(7,9))
# print(add_subtract(-4,6))


# def name(a):
#     print(a + " chauhan")

# name("shivani")
# name("priya") 
# name("deepika")
# name("riya")
# name("shweta")
# name("payal") 


# print(float(46,9))
# def float(a,b):
#     if a % b == 0:
#         return True
#     else:
#         return False

# print(float(4,2))
# print(float(8,9))
# print(float(37,21))
# print(float(200,10))
# print(float(36,8))

  
# def even(v):
#     a = 1
#     while a <= v:
#         if a % 2==0:
#             print(a)
#         a+=1
# even(2)
# even(6)
# even(7)
# even(9)
# even(10)

# def sum(a,b):
#     print(a+b)
# sum(1,3)
# print("-----------------")
# sum(8,2)
# print("-----------------")
# sum(9,6)
# print("-----------------")
# sum(20,16)
# print("-----------------")
# sum(90,10)
# print("-----------------")
# sum(36,38)


# def float(a,b):
#     if a % b == 0:
#         return True
#     else:
#         return False
# print(float(20,10))
# print("-----------------")
# print(float(55,60))
# print("-----------------")
# print(float(16,6))
# print("-----------------")
# print(float(22,12))
# print("-----------------")
# print(float(30,12))
# print("-----------------")
# print(float(46,36))

# 1. Write a Python function to find the maximum of three numbers.
# def maxOfThree(x,y,z):
#     if x>=y:
#         max = x
#     else:
#         max = y
#     if max >= z:
#         return max
#     else:
#         return z
    
# print(maxOfThree(2,7,8))

# 2. Write a Python function to sum all the numbers in a list.

# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total = total + x
#     return total
# print(sum((2,6,8,4)))
# print(sum((3,7,5,9)))
# print(sum((12,14,16,18)))
# print(sum((20,16,18,16)))

# 3. Write a Python function to multiply all the numbers in a list.
# def multi(numbers):
#     multiply = 1
#     for x in numbers:
#         multiply = multiply*x
#     return multiply
# print(multi((10,2,3,4)))
# print(multi((16,4,6,20)))
# print(multi((2,40,10,16)))
# print(multi((10,30,40,60)))

# 4. Write a Python program to reverse a string.
# def reverse(string):
#     return string[::-1]
# print(reverse("shivani"))
# print(reverse("mohit"))
# print(reverse("sobhit"))
# print(reverse("sagar"))
# print(reverse("shweta"))
# print(reverse("gargi"))

# 5.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(6))
# print(factorial(8))
# print(factorial(10))
# print(factorial(20))

# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brown Fox'

# def upperLowerCount(string):
#     Upper = 0
#     Lower = 0
#     for x in string:
#         if x.isupper():
#             Upper = Upper+1
#         if x.islower():
#             Lower = Lower+1
#     return Upper,Lower
# print(upperLowerCount("a Quick Brown Fox"))
# print(upperLowerCount("A dog is A pet Animal"))


# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# def newList(l):
#     l1 = []
#     for x in l:
#         if x not in l1:
#             l1.append(x)
#     return l1
# print(newList([1,2,1,3,4,4,6,6,6,8,8]))
# print(newList([2,8,9,8,3,3,4,4,6,16,20]))


# 10. Write a Python program to print the even numbers from a given list.
# def even(l):
#     l1 = []
#     for x in l :
#         if x % 2 == 0:
#             l1.append(x)
#     return l1
# print(even([2,17,19,18,22,25,26,30]))
# print(even([12,13,26,24,30,39,38])) 
# print(even([12,60,30,33,28,25,37,55,56]))            

# def outer():
#     print("outer function started")
#     def inner():
#         print("inner function execution")
#     print("outer function returning inner function")
#     return inner
# f1=outer()
# print(f1)
# print(id(f1))
# f1()
# f1()

# def inner():
#     print("inner function execution")
# f1 = inner
# print(f1)

def greet ():
    print("how are you")
    print("what is your name")
    print("apple")

greet()
greet()