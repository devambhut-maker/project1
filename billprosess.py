# Item 1
item1 = input("Enter Item 1: ")
price1 = float(input("Enter Price 1: "))
qty1 = int(input("Enter Quantity 1: "))

# Item 2
item2 = input("Enter Item 2: ")
price2 = float(input("Enter Price 2: "))
qty2 = int(input("Enter Quantity 2: "))

# Calculation
cost1 = price1 * qty1
cost2 = price2 * qty2
total = cost1 + cost2
discount = total * 10 / 100
final = total - discount

discount = float(input("Enter Discount (%): "))

# Output
print("\n--- Bill ---")
print(item1, ": ₹", cost1)
print(item2, ": ₹", cost2)
print("Total Bill: ₹", total)
print("Discount (10%): ₹", discount)
print("Final Price: ₹", final)