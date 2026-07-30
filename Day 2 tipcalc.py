#Tip Calculator
print("Welcome to the tip Calculator! ")
total_bill=float(input("What was th etotal bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people=int(input("How many people spilt the bill? "))
pay=(total_bill+(((tip)/100)*total_bill))/no_of_people
print(f"Each person should pay: ${round(pay,2)} ")
