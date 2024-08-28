print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_in_value = bill * tip/100
total_bill_including_tip  = tip_in_value + bill

each_person_pays = total_bill_including_tip / people

rounding_each_person_bill = round(each_person_pays , 2)

print(f"Each person should pay: {rounding_each_person_bill}")
