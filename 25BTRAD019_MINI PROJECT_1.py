# Simple Bill Generator

print("====== BILL GENERATOR ======")

item1 = input("Enter Item 1: ")
qty1 = int(input("Enter Quantity: "))
price1 = float(input("Enter Price: "))

item2 = input("\nEnter Item 2: ")
qty2 = int(input("Enter Quantity: "))
price2 = float(input("Enter Price: "))

total1 = qty1 * price1
total2 = qty2 * price2
grand_total = total1 + total2

print("\n========== BILL ==========")
print(f"{'Item':<12}{'Qty':<8}{'Total'}")
print("-" * 28)
print(f"{item1:<12}{qty1:<8}₹{total1:.2f}")
print(f"{item2:<12}{qty2:<8}₹{total2:.2f}")
print("-" * 28)
print(f"Grand Total: ₹{grand_total:.2f}")
print("==========================")