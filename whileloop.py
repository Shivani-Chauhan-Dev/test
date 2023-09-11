# i = 1
# while i < 6:
#   print(i)
#   i += 1
# print("finish")
# while(i < 6){
#  print(i)
#   i += 1
# }
# print("finish")


# v = 1
# while v < 101 :   
#     print(v)
#     v += 1



# v = 2
# while v < 21:
#   print(v)
#   v += 2


# v = 1
# while v < 20:

# num = 1
# while num < 11:
#   print(num)
#   num += 1


# num = 0 
# while num < 10:
#   print(num)
#   num += 1


# int = 1
# while int < 11:
#   print(int)
#   int += 1 


# num = 10
# while num < 301:
#   print(num)


#   num += 10


# series = 105
# while series > 6:
#   print(series)
#   series -= 7


# natural = 10
# while natural > 0:
#   print(natural)
#   natural -= 1


#   num = 1
#   sum = 0
#   while num <= 10:
#     sum += num
#     num += 1
#     print(sum)



# natural = 20
# sum = 0
# while natural >= 2:
#   sum += natural
#   natural -= 2
#   print(sum)

# program to find the product of the digit of a number accepted from the user

# i = 1
# s = int(input("number entered from the user: "))
# while i <= 10:
#   print(s * i)
#   i += 1

s = [4 , 8, 16 , 24, 18 , 7 , 25 , 30]
i = 0
for x in s :
    while i <= x:
        if x % 2 == 0:
            print("this is the power of 2", x)
        else:
            print("not a power of 2")
        i += 1
