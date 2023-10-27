# Input: Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculating tip (18% of food charge)
tip_percentage = 0.18
tip_amount = food_charge * tip_percentage
# Calculating sales tax (7% of food charge)
tax_percentage = 0.07
tax_amount = food_charge * tax_percentage