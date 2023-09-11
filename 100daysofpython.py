print("Welcome! in our band")
city = input("enter the city name that they grew up:\n ")
pet = input("enter the pet name:\n ")
print("Your band name could be: " + city + " " + pet)

# 2nd 
print("Welcome to the tip calculater.")
bill = float(input("what was the totle bill:  $"))
tip = int(input("how much tip would you like to give ? 10, 20 or 15 ?"))
people = int(input("how many people split the bill: "))
tip_as_percent = tip / 100
total_tip_amount = bill + tip_as_percent
total_bill_amount = bill + total_tip_amount
bill_each_person = total_bill_amount / people
final_amount = round(bill_each_person,2)
print(f"each person should pay : ${final_amount}")

