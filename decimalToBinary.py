def decimal(a):
    print(bin(a))
decimal(3)
decimal(400)
decimal(6784)

def decimaltobinary(a):
    if a >= 1:
        decimaltobinary(a / 2)
        print(a % 2)
        
         

decimaltobinary(70)        
decimaltobinary(40098)
decimaltobinary(4098)
decimaltobinary(17)
decimaltobinary(366)


def decimaltooctal(num):
    if num >= 1:
        decimaltooctal(num / 8)
        print(num % 2)
print("-----------")
decimaltooctal(24)
print("--------------")
decimaltooctal(36)
print("------------")
decimaltooctal(466)
print("-------------")
decimaltooctal(266)
print("-----------")
decimaltooctal(3266)        
    
    

