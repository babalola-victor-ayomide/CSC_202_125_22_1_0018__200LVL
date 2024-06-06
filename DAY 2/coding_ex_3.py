print("Welcome to the tip calculator.")
bill = float(input("what was the total bill? $"))
tip= int(input("what percentage tip would you like to give? 10, 12, or 15? "))
person= int(input("How many people to split the bill?")) 
tip_as_percent = tip/100
precent_of_bill= bill*tip_as_percent
total_bill= bill+ precent_of_bill
payment= total_bill/person
final_amount=  "{:.2f}".format(payment)
print(f"Each person should pay: ${final_amount}")

