#Item listing
total_amount = 0
item1 = input("Enter the name of your first item:")
quantity1 = int(input("Enter the quantity of the items you want to buy:"))
price1 = float(input("Enter the price of the first item:"))
item1_total = quantity1*price1
total_amount += item1_total

item2 = input("Enter the name of your second item:")
quantity2 = int(input("Enter the quantity of the items you want to buy:"))
price2 = float(input("Enter the price of the second item:"))
item2_total = quantity2*price2
total_amount += item2_total

item3 = input("Enter the name of your third item:")
quantity3 = int(input("Enter the quantity of the items you want to buy:"))
price3 = float(input("Enter the price of the third item:"))
item3_total = quantity3*price3
total_amount += item3_total

#Results
print(f"{item1} X {quantity1}: \u00A3{item1_total:.3f}")
print(f"{item2} X {quantity2}: \u00A3{item2_total:.3f}")
print(f"{item3} X {quantity3}: \u00A3{item3_total:.3f}")
print(f"The total amount of the items is: \u00A3{total_amount:.3f}")
print("New addition")

# Conlcusion



