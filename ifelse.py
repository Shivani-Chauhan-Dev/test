# # first program
# light = "green"
# if light != "green" :
#     print("please stop")
# else :
#     print("you can go")

# # second program
# age=10
# if age < 18:
#    print("you can fire")
# else:
#     print("you can go")

# third program
# age = 26 
# if age != 26:
#     print ("you can go")
# else:
#     print ("you can not go")    
    
# # fourth program
# number = 10
# if number >= 0:
#     print(" positive number")    
# else:
#     print("negative number")
#     print("this statement is always executed")

# # fifth program
# a = "b"
# if a > "b":
#     print("she is girl")
# else:
#     print("he is boy")
# print("this statement is always executed")        

# # sixth program
# # program to find the biggest of given 2 numbers from the keyboard 

# # n1 = int(input("enter the first integer number: "))
# n2 = int(input("enter the second integer number: "))
# if n1 > n2 :
    # print("bigger number:", n1)
# else:
    # print("bigger number:", n2)    

# seventh program
# program to find the biggest of given 3 number from the keyboard
# write a program to find maximum and minimum element  of given list the list is entered by the 
# while True:
    # a = input("enter the list of integer values seperated by comma :")
# print(a,type(a))
# print(str(a),type(str(a)))

    # b = eval(a)
    # print("max value: ",max(b))
    # print("mini value: ",min(b))

# list = [40,2,80,60]
# print(max(list))
# print(min(list)) 

# we check the numbers between 1 to 100

# s =int(input("entered integer number from the user: "))
# if 1 <= s <= 100:
#     print("this number is between 1 to 100")
# else:
#     print("this number is not between in 1 to 100")    
# import sys
# my_variable = -sys.maxsize - 1
# print(my_variable)

# 3rd
print("Welcome! to tresure island.")
print("Your mission is find the treasure.")
choice1 = input("You \'re at a crossroad.where do u want to go ? Type 'left' or 'right'. \n").lower()
if choice1 == "left":
    choice2 =input("""You have come to a lake . There is an island in the middle of a lake. Type 'Wait' to wait for a boat. 
                   Type 'Swim' to swim across\n""").lower()
    if choice2 == "wait":
        choice3 = input("""you arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue. Which colour
                        do u choice\n""").lower()
        if choice3 == "red":
            print("it's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure.You win.")
        elif choice3 == "blue":
            print("you enter the room of beasts .Game over.")
        else:
            print("you chosse a door that does not exist. Game over.")

    else:
        print("You got attecked by an angry trout. Game Over.")
else:   
    print("You fell into a hole. Game Over.")
   
  

