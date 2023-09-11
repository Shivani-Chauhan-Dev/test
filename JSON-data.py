import json
# 1. Write a Python program to convert JSON data to Python object.
# jsondata = '{ "Name":"David", "Class":"I", "Age":6 }'
# y = json.loads(jsondata)
# print(y)
# print(y["Name"])
# print(y["Class"])
# print(y["Age"])


# 2. Write a Python program to convert Python object to JSON data.
# pythondata = {
#   "name": "David",
#   "class":"I",
#   "age": 6  
# }
# y = json.dumps(pythondata)
# print(y)
# print(type(y))

# 3. Write a Python program to convert Python objects into JSON strings. Print all the values.
# python_dict =  {"name": "David", "age": 6, "class":"I"}
# python_list =  ["Red", "Green", "Black"]
# python_str =  "Python Json"
# python_int =  1234
# python_float =  21.34
# python_T =  True
# python_F =  False
# python_N =  None


# json_dict = json.dumps(python_dict)
# json_list = json.dumps(python_list)
# json_str = json.dumps(python_str)
# json_int = json.dumps(python_int)
# json_float = json.dumps(python_float)
# json_T = json.dumps(python_T)
# json_F = json.dumps(python_F)
# json_N = json.dumps(python_N)

# print("json dict : ", json_dict)
# print("jason list : ", json_list)
# print("json string : ", json_str)
# print("json number1 : ",json_int )
# print("json number2 : ",json_float )
# print("json true : ", json_T)
# print("json false : ", json_F)
# print("json null ; ", json_N)


# 4. Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
# pythondic = {"1":3,"6":5,"4":4,"2":6}
# y = json.dumps(pythondic, sort_keys=True,indent=4)
# print(y)
# print(type(y))

# 5. Write a Python program to convert JSON encoded data into Python objects.
json_dict =  '{"name": "David", "age": 6, "class": "I"}'
json_list =   '["Red", "Green", "Black"]'
json_string = '"Python Json"'
json_int = '1234'
json_float =  '21.34'

python_dict = json.loads(json_dict)
python_list = json.loads(json_list)
python_string = json.loads(json_string)
python_int = json.loads(json_int)
python_float = json.loads(json_float)

print(python_dict)
print(python_list)
print(python_string)
print(python_int)
print(python_float)