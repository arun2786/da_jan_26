print("======== Welcome to my shop ========")
print("============= Our menu =============")
print("")

item_pirces = [15, 25, 99, 150]
item_names = ["Samosa", "Burger", "Pizza", "Cake"]
item_quantities = []
item_bills = []

for i in range(len(item_names)):
    item_quantities.append(0)
    item_bills.append(0)

# samosa_price = 15
# tea_price = 10
# burger_price = 25
# pizza_price = 99

# print("1. Samosa\t- Rs",samosa_price)
# print("2. Tea\t\t- Rs",tea_price)
# print("3. Burger\t- Rs",burger_price)
# print("4. Pizza\t- Rs",pizza_price)
for i in range(len(item_names)):
    print(f"{i+1}. {item_names[i]}\t- Rs{item_pirces[i]}")
print("")

# samosa_quantity = int(input("Enter samosa quantity: "))
# tea_quantity = int(input("Enter tea quantity: "))
# burger_quantity = int(input("Enter burger quantity: "))
# pizza_quantity = int(input("Enter pizza quantity: "))
for i in range(len(item_names)):
    item_quantities[i] = int(input(f"Enter {item_names[i]} quantity: "))

print("")

# samosa_bill = samosa_price * samosa_quantity
# tea_bill = tea_price * tea_quantity
# burger_bill = burger_price * burger_quantity
# pizza_bill = pizza_price * pizza_quantity

for i in range(len(item_names)):
    item_bills[i] = item_pirces[i] * item_quantities[i]

print("Item\tQuantity\tPrice\tTotal")
print("---------------------------------------")
# print("Samosa\t",samosa_quantity,"\t\tRs ",samosa_price,"\tRs ",samosa_bill)
# print("Tea\t",tea_quantity,"\t\tRs ",tea_price,"\tRs ",tea_bill)
# print("Burger\t",burger_quantity,"\t\tRs ",burger_price,"\tRs ",burger_bill)
# print("Pizza\t",pizza_quantity,"\t\tRs ",pizza_price,"\tRs ",pizza_bill)
for i in range(len(item_names)):
    print(f"{item_names[i]}\t{item_quantities[i]}\t\tRs {item_pirces[i]}\tRs {item_bills[i]}")
print("---------------------------------------")
print("")

total_bill = 0
for i in range(len(item_names)):
    total_bill = total_bill + item_bills[i]
print("Total bill:", total_bill)
