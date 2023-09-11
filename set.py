# s = {10,20,39,30,40,50}
# print(s)
# print(type(s))

# list = [10,30,30,40,50,10,10]
# t = set(list)
# print(t)

# s = set(range(1,10))
# print(s)

# function of set

# add(x)
# s = {10,20,30,40}
# s.add(60)
# s.add(80)
# s.add(68)
# print(s)

# update(x,y,z)
# s = {10,20,30}
# l = [20,30,41,28]
# t = (20,9,6,8)
# s.update(l,t,range(100,110))
# print(s)

# copy()
# s = {10,20,3,40}
# print(id(s))
# s1 = s.copy()
# print(id(s1))
# print(s1)

# pop()
# s = {10,20,39,30,40}
# print(s)
# print(s.pop())
# print(s)

# remove()
# s ={10,20,30,40,50,60}
# s.remove(60)
# print(s)

# discard()
# s={10,20,30,40}
# s.discard(80)
# print(s)

#  clear()
# s = {10,40,50,60,70,80}
# s.clear()
# print(s)


# Mathematical operations on the Set:
# 1.union():
# x = {10,20,30,40}
# y = {30,60,80,90,100,406}
# print(x.union(y))
# print(x|y)

# 2. intersection():
# x={10,20,30,40}
# y={30,40,50,60}
# print(x.intersection(y))
# print(x&y)

# 3. difference():
# x={10,20,30,40}
# y={30,40,50,60}
# print(x.difference(y))
# print(x-y)

# 4.symmetric_difference():
# x={10,20,30,40}
# y={30,40,50,60}
# print(x.symmetric_difference(y))
# print(x^y)

# Set Comprehension
# s ={x**2 for x in range(1,20)}
# print(s)

# 1. Write a Python program to create a set.
# s = set()
# print(s)


# 2. Write a Python program to iterate over sets.
# set = {10,30,60,50,70,80}
# for x in set:
#     print(x)


# 3. Write a Python program to add member(s) to a set.
# set = {10,30,40,50,60}
# set.add(36)
# print(set)

# 4. Write a Python program to remove item(s) from a given set.
# set = {10,30,28,60,70,20,40,90}
# set.pop()
# print(set)

# 5. Write a Python program to remove an item from a set if it is present in the set.
# set = {10,40,50,20,90,100,70,16}
# set.remove(10)
# print(set)


# 6. Write a Python program to create an intersection of sets.
# s1 = {10,50,60,56,68}
# s2 = {10,50,60,36,56}
# print(s1&s2)


# 7. Write a Python program to create a union of sets.
# s1 = {10,50,56,48,16,36}
# s2 = {16,76.10,20,18,20}
# print(s1|s2)

# 8. Write a Python program to create set difference.
# s1 = {10,49,57,79,5487,24,40,50,60}
# s2 = {10,30,50,20,60,57,7}
# print(s1-s2)


# 9. Write a Python program to create a symmetric difference.
# s1 = {10,20,40,30,59,68,80}
# s2 = {10,60,30,20,70,56,20}
# print(s1^s2)


# 10. Write a Python program to check if a set is a subset of another set.
# S1 = {10,20,40,50,60,70,80}
# S2 = {20,60,70,40}
# t=S2.issubset(S1)
# print(t)


# 12. Write a Python program to remove all elements from a given set.
# set = {10,30,40,50,60,70,80,90}
# set.clear()
# print(set)


# 13. Write a Python program that uses frozensets.
# x = frozenset([1, 2, 3, 4, 5])
# y = frozenset([3, 4, 5, 6, 7])
# print(x&y)


# 14. Write a Python program to find the maximum and minimum values in a set.
# set = {10,60,70,20,90,16,6}
# print(max(set))
# print(min(set))


# 15. Write a Python program to find the length of a set.
# set = {10,40,50,60,340,50,16}
# print(len(set))


# 16. Write a Python program to check if a given value is present in a set or not.
# n = input("enter the letter from the user: ")
# set = {"a","b","c","g","d","s","m","o"}
# if n in set:
#     print(True)
# else:
#     print("not exit")


# 17. Write a Python program to check if two given sets have no elements in common.
# set1 = {10,20,30,40,50,60}
# set2 = {70,80,11,16,24,26}
# print(set1&set2)
# print("not comman element in both set")


# 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.
# s = {10,20,30,40,50,60}
# print(s.issuperset(s))
# s1 = {10,30,40}
# print(s.issuperset(s1))


# 19. Write a Python program to find elements in a given set that are not in another set.
# set1 = {1,5,7,8,9,13,16}
# set2 = {1,5,6,13,18,20,22}
# t = set1.difference(set2)
# print(t)
# l = set2.difference(set1)
# print(l)


# 20. Write a Python program to remove the intersection of a second set with a first set.
# set1 = {1,4,68,8,4,9,10}
# set2 = {3,6,7,8,5,4,10,12}
# t = set1.intersection_update(set2)
# print(t)dout


# Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set
# set1 = {1,2,4,10,39,29,37,16}
# set2 = {3,4,1,3,30,20,10,16,18}
# print("missing in second set:", set1 - set2)
# print("missing in first set: ",set2-set1)


# 30. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.
# list = ["a","v","w","s","w","s","m","p","z","a"]
# t=set(list)
# print(t)
# print(list(t))dout


# 29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.
# set1 = {10,30,50,40,60,80,90}
# t = list(set1)
# t.sort(reverse=True)
# print(t)
# print(t[2])

# 10. Python Set Exercise with Solutions
# Exercise 1: Add a list of elements to a set
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# print(sample_set)

# Exercise 2: Return a new set of identical items from two sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# y = set1.intersection(set2)
# print(y)

# Exercise 3: Get Only unique items from two sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# y = set1.union(set2)
# print(y)

# Exercise 4: Update the first set with items that don’t exist in the second set
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)

# Exercise 5: Remove items from the set at once
# set1 = {10, 20, 30, 40, 50}
# set2={10,20,30}
# set1.difference_update(set2)
# print(set1)


# Exercise 6: Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# y=set1.symmetric_difference(set2)
# print(y)

# Exercise 6: Check if two sets have any elements in common. If yes, display the common
# elements
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}
# y = set1.intersection(set2)
# print(y)

# Exercise 7: Update set1 by adding items from set2, except common items
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# set1.symmetric_difference_update(set2)
# print(set1)

# Exercise 8: Remove items from set1 that are common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)