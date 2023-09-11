# def old ():
#     print("1 line")
#     print("2 line")

# def decorater(old):
#     def new():
#         old()
#         print("3 line")
#         print("4 line") 
#     return new
# old()
# print("-------------")
# l = decorater(old)
# l()

# 2nd program

# def newfunc():
#     print("say hello")

# def decorator(newfunc):
#     def wrapper():
#         print("something is happening after function is called")
#         newfunc()
#         print("something is happening before the function is called")
#     return wrapper


# newfunc()
# print("----------")
# l = decorator(newfunc)
# l()

# program - 2 nd method 
def decorator(newfunc):
    def wrapper():
        print("something is happening before function is called")
        newfunc()
        print("something is happening after hte function is called")
    return wrapper
@decorator
def newfunc():
    print("say hello")

newfunc()

