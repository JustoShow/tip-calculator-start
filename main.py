#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator!\n")
bill = input("What's the bill total? ")
number_of_people = input("How many people will split the bill? ")
tip = input("What is the tip percentage (ie. 10, 15, 20)? ")
bill_with_tip = round(float(bill) * ((int(tip) / 100) + 1), 2)
each_person_pay = round(bill_with_tip / int(number_of_people), 2)

print(f"\nThe total bill is ${bill_with_tip:.2f}\nEach person should pay ${each_person_pay:.2f}.")