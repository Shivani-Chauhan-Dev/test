from functools import *
# result = reduce(lambda x,y:x+y,range(1,101))
# print(result)

result = reduce(lambda x: x**2,range(1,11))
print(result)