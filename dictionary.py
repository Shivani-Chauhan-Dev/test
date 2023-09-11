# thisdict = {"shivani": "chauhan", "age": 30, "fruit": "apple"}
# print(thisdict)

# print(thisdict["shivani"])

# # length of dictionary
# print(len(thisdict))

# print(thisdict["fruit"])

# # type of dictionary
# print(type(thisdict))

# # get()
# print(thisdict.get("shivani"))

# print(thisdict.get("age"))

# print(thisdict.get("fruit"))

# # the dict() constructor
# file =dict (age = 26, village = "mamepur", colour = "blac") 
# print(file)

# # get keys()
# x = thisdict.keys()
# print(x)

# # before the change
# file = {"age":26, "village":"mamepur", "colour":"black"} 
# x = file.keys()
# print(x)

# # after the change
# file["black"] = 30
# print(x)

# x = thisdict.values()
# print(x)

# # before the change
# x = file.values()
# print(x)

# # after the change
# file["vegetable"] = "potato"
# print(x)

# # get items()
# x = file.items()
# print(x)

# car = {"shivani":"chauhan", "age":56, "water":"animal"}
# x = car.items()
# print(x)

# car["year"] = 16
# print(x)

# # check if key exists
# life = {"name":"shivani", "class":2, "table":"chair", "number":26}
# if "name" in life:
#     print("yes, 'name' is one of the keys in the life dictionary")

#     print("yes, 'table' is one of the keys in the life dictionary ")

# # python change dictionary items

# # change values

# dog = {"brand":"ford", "modle":"mustang", "year":1964}
# dog["year"] = 2022
# print(dog)

# # update dictionary = update()
# x = dog.update({"year":2022})
# print(x)

# # python add dictionary items
# # adding items

# cat = {"year":2022, "name":"shivani", "class":"msc", "hindi":"language"}
# cat["willem"] = "mikal"
# print(cat)

# cat["colour"] = "red"
# print(cat)

# # python remove dictionary items
# # removing items

# # pop()

# boy = {"boy":"girl", "age":26, "book":"pen", "year":2023}
# x = boy.pop("boy")
# print(x)

# # popitems()

# boy.popitem()
# print(boy) 

# # clear()

# thisdict = {"brand":"foard", "model":"mastang", "year":2023}
# thisdict.clear()
# print(thisdict)

# # python - loop dictionary
# # loop through a dictionary

# # print all keys name in the dictionary one by one
# boy = {"boy":"girl", "age":26, "book":"pen", "year":2023}
 
# for x in boy:
    # print(x)

# for x in boy.keys():
#     print(x)

# # print all values name in the dictionary one by one

# for x in boy:
#     print(boy[x])

# for x in boy.values():
#     print(x)

# # loop for items()

# for x in boy.items():
#     print(x)


# # python  - nested dictionaries
# # nested dictionary
# # mydict = {"child1":{"name":"emil", "year":1996}, "child2":{"name":"tosib", "year":1997}, "child3":{"name":"wilyam", "year":1998}}
# # print(mydict)


# # creat one dictionary that will contain the other three dictionary
# child1 = {"name":"emil", "year":1996}
# child2 = {"name":"tosib", "year":1997}
# child3 = {"name":"wilyam", "year":1998}
# myfamily = {"child1":child1, "child2":child2, "child3":child3}
# print(myfamily)


# How to create Dictionary
# d ={}
# d[100] = "shiva"
# d[200] = "shweta"
# d[300] = "mohit"
# d[400] = "ashok"
# print(d)

# How to access data from the dictionary
# d={100:'durga' ,200:'ravi', 300:'shiva'}
# print(d[100])
# print(d[200])
# print(d[600])

# How to update dictionaries
# d={100:'durga' ,200:'ravi', 300:'shiva'}
# d[100] = "shivani"
# d[300] = "mohit"
# print(d)

# d={100:"durga",200:"ravi",300:"shiva"} 
# del d[100]
# del d[300]
# print(d)
# del d
# print(d)


# d.clear()

# d={100:"durga",200:"ravi",300:"shiva"} 
# print(d)
# d.clear()
# print(d)

# Important functions of dictionary

# len()
# d={100:"durga",200:"ravi",300:"shiva",400 :"mohit"}
# print(len(d)) 

# pop():
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.pop(100))
# print(d)
# d.pop(600)
# print(d)

# keys()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.keys())
# for x in d.keys():
#     print(x)

#  values():
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.values())
# for x in d.values():
#     print(x)

# items()
# d={100:"durga",200:"ravi",300:"shiva"}
# print(d.items())
# for x in d.items():
#     print(x)

# setdefault()
# d={100:"durga",200:"ravi",300:"shiva"}
# d.setdefault(600,"mohit")
# print(d)


# Q. Write a program to take dictionary from the keyboard and print the sum of values
# dic = eval(input("enter the dictionary from the user: "))
# sum = 0
# for x in dic.values():
#     sum = sum + x
# print(sum)   

# Dictionary Comprehension:
# squares = {x:x**2 for x in range(1,10)}
# print(squares)

# doubles = {x:x*2 for x in range(1,16)}
# print(doubles)

# merge dictionary
# one = {1: 'a', 2: 'b', 3: 'c'}
# two = {4: 'd', 5: 'e', 6: 'f'}
# one.update(two)
# print(one)

# Add values
# one = {1: 'a', 2: 'b', 3: 'c'}
# one[4]="d"
# one[5]="e"
# one[6]="f"
# print(one)

# one.update({4:"d",5:"e",6:"f"})
# print(one)

# old_stock = {'water': 1.42, 'cheese': 2.5, 'milk': 2.0}
# price = 0.76
# for x in old_stock.items():
#     print(x)
# new= {item:value*price for (item ,value) in old_stock.items()}
# print(new)


# find length of variable
# names = ['Alex', 'Tom', 'Johnson', 'Bi', 'Foobar']
# name = {x:len(x) for x in names}
# print(name)

# nested dictionary comperihension 2
# keys =['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# new = {k1:values for k1 in keys }
# print(new)

# nested dictionary comperihension 1
# keys =['a', 'b', 'c', 'd']
# values = [1, 2, 3]
# new={k1:{x:k1 for x in values} for k1 in keys}
# print(new) 


# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

# dic = {1:"a",5:"c",3:"d",2:"b"}
# for key in sorted(dic)
# print(dic)dout


# 2. Write a Python script to add a key to a dictionary.
# dic = {1:"a",2:"c",3:"d"}
# dic.update({4:"d"})
# print(dic)
# dic[6]="s"
# print(dic)


# 3. Write a Python script to concatenate the following dictionaries to create a new one.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic = {}
# for x in dic1,dic2,dic3:
#     dic.update(x)
# print(dic)


# 4. Write a Python script to check whether a given key already exists in a dictionary.
# dic = {2:"sh",1:"iv",4:"an",6:"ph"}
# d = int(input("enter the key from the user: "))
# if d in dic:
#     print(d,"present in the dictionary")
# else:
#     print(d,"not present in the dictionary")


# 5. Write a Python program to iterate over dictionaries using for loops.
# dic = {2:"sh",1:"iv",4:"an",6:"ph"}
# for x in dic.items():
#     print(x)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# n = int(input("enter the number from the user: "))
# dic = {x:x**2 for x in range(1,n+1)}
# print(dic)


# 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# dic = {x:x**2 for x in range(1,16)}
# print(dic)

# 8. Write a Python script to merge two Python dictionaries.
# dic1 = {1:"a",2:"b",3:"c"}
# dic2 = {4:"d",5:"e",6:"f"}
# dic1.update(dic2)
# print(dic1)

# 9. Write a Python program to iterate over dictionaries using for loops.
# dic = {1:"ab",2:"bc",3:"cd",4:"de",5:"ef",6:"fg"}
# for x in dic.items():
#     print(x)


# 10. Write a Python program to sum all the items in a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}
# sum = 0
# for x in my_dict.values():
#     sum = sum + x
# print(sum)

# 11. Write a Python program to multiply all the items in a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}
# multiply = 1
# for x in my_dict.values():
#     multiply = multiply*x
# print(multiply)


# 12. Write a Python program to remove a key from a dictionary.
# my_dict = {'data1':100,'data2':-54,'data3':247}
# my_dict.pop("data1")
# print(my_dict)


# 13. Write a Python program to map two lists into a dictionary.
# one = [1, 2, 3, 4, 5]
# two = ['a', 'b', 'c', 'd', 'e']
# new = dict(zip(one,two))
# print(new)


# 14. Write a Python program to sort a given dictionary by key.
# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
# for x in sorted (color_dict):
#     print(x ,color_dict[x])


# 15. Write a Python program to get the maximum and minimum values of a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
print(max(my_dict.items()))
print(min(my_dict.items()))