
# This program calculates the total amount of a meal purchased at a restaurant.
# The program ask the user to enter the charge for the food, and amount of tip and 0.975 percent sales tax.
# Will display each of these amounts and the total

cost = float( input ("Enter the total amount of the meal: $"))
tipRate = float( input ("Enter the tip: %"))
tipRate = tipRate/100
sales_tax = 0.0975  # Alameda county
tip = cost * tipRate
tax = cost * sales_tax
total = cost + tip + tax
print ("\nTip:            $", format(tip, '.2f'))
print ("Sales tax:      $", format(tax, '.2f'))
print ("Total:          $", format(total, '.2f'))