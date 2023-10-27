# Input: Ask the user to enter the charge for the food
food_charge = float(input("Enter the charge for the food: $"))

# Calculating tip (18% of food charge)
tip_percentage = 0.18
tip_amount = food_charge * tip_percentage
# Calculating sales tax (7% of food charge)
tax_percentage = 0.07
tax_amount = food_charge * tax_percentage
# Calculating grand total (food charge + tip + sales tax)
grand_total = food_charge + tip_amount + tax_amount

# Display the results
print('Tip = $',round(tip_amount, 2))
print('Sales tax = $',round(tax_amount, 2))
print('Grand Total = $',round(grand_total, 2))